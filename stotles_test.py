#!/usr/bin/env python3
import requests
import json
import sqlite3
import os.path
import configparser
import sys

## Calling Config File for DB_Name,Query,URL,RequestBody,OutputFilename
config = configparser.ConfigParser()
config.read('config.ini')

## Setting URL
def _url(path):
    return config['WEB']['v_URL'] + path

##Post Notices
def Func_POST_Notices(task):
    return requests.post(_url('/search_notices/json'),json=task)

## Setting Path from base directory
def Func_Path_Set(Name):
    BASE_DIR= os.path.dirname(os.path.abspath(__file__))
    return os.path.join(BASE_DIR,Name)


## Retrieving required fields from JSON response
def Func_Parse_Notices(res):
    data=res.json()
    result = []
    for items in data['noticeList']:
        my_dict={}
        my_dict['title']=items.get('item').get('title')
        my_dict['publishedDate']=items.get('item').get('publishedDate')
        my_dict['organisationName']=items.get('item').get('organisationName')
        my_dict['noticeType']=items.get('item').get('noticeType')
        my_dict['description']=items.get('item').get('description')
        my_dict['start']=items.get('item').get('start')
        my_dict['end']=items.get('item').get('end')
		## Select AwardDate for Awards
        if (my_dict['noticeType'].lower() == "awards"):
            my_dict['awardedDate']=items.get('item').get('awardedDate')
		## Select DeadlineDate for Tenders
        if (my_dict['noticeType'].lower() == "tenders"):
            my_dict['deadlineDate']=items.get('item').get('deadlineDate')
        result.append(my_dict)
    return result


## To save the result of API in JSON format
def Func_json_save(resp):
    res=Func_Parse_Notices(resp)
    back_json=json.dumps(res)
    Filename = Func_Path_Set(config['OUTFILE']['v_JSON_File'])
    File1 = open('%s' %Filename ,'w')  ## File opened in Write Mode and not Append Mode
    File1.write(back_json)
    File1.close
    return Filename
	

## User Input text for StartDate,EndDate and Description
def Func_User_Input(Opt):
    if(Opt == 3): 
     Description = input("Enter Description or Substring of Description  :")
     return Description
    elif(Opt== 2):
     Start_date = input("Enter Start Date:(YYYY-MM-DD) Eg.12-Jan-2020 is 2020-01-12  :")
     End_date = input("Enter End Date(YYYY-MM-DD) Eg.12-Jan-2020 is 2020-01-12  :")
     return Start_date,End_date
    else:
     print("Invalid Option")
     


## Setting Default Value for every row inserted in DB
def Func_Default_DB_val():
   my_dict={}
   my_dict['title']=""
   my_dict['publishedDate']=0
   my_dict['organisationName']=""
   my_dict['noticeType']=""
   my_dict['deadlineDate']=0
   my_dict['awardedDate']=0
   my_dict['description']=""
   my_dict['start']=0
   my_dict['end']=0
   return my_dict


## Search Notices between start date and end date
def Func_Search_btw_dates(resp,start_date=0,end_date=0):
   res=Func_Parse_Notices(resp)
   my_dict={}
   result=[]
   for my_dict in res:
     if (start_date!=0 and my_dict['start'] >= start_date) and (end_date!=0 and my_dict['end'] <= end_date):
        result.append(my_dict)
   return result


## Search Notices for description or part of description
def Func_Search_desc(resp,desc=""):
   res=Func_Parse_Notices(resp) 
   my_dict={}
   result=[]
   for my_dict in res:
     if (desc!='' and desc.lower() in my_dict['description'].lower()):
        result.append(my_dict)
   return result


##  Function to create table if not exist
def Func_create_table(cur):
    cur.execute("Create Table if not exists notices ('Title' TEXT DEFAULT '', 'PublishedDate' INTEGER DEFAULT 0,'OrganisationName' TEXT DEFAULT '','NoticeType' TEXT DEFAULT '', 'DeadlineDate' INTEGER DEFAULT 0, 'AwardedDate' INTEGER DEFAULT 0, 'Description' TEXT DEFAULT '', 'StartDate' INTEGER DEFAULT 0, 'EndDate' INTEGER DEFAULT 0)")


## Function to delete previous data and store the result of API in table
def Func_Save_DB(resp):
    res=Func_Parse_Notices(resp)
    DB_PATH = Func_Path_Set(config['SQLITE']['v_DBName'])
    my_dict = Func_Default_DB_val()
    
    
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        Func_create_table(cursor)
        cursor.execute("Delete from notices")
        connection.commit()
    
    count_rows = 0    
    for my_dict1 in res:
        count_rows = count_rows + 1
        for key in my_dict1:
            my_dict[key]=my_dict1[key]

        cursor.execute("Insert into notices values (?,?,?,?,?,?,?,?,?)",(my_dict['title'],my_dict['publishedDate'],my_dict['organisationName'],my_dict['noticeType'],my_dict['deadlineDate'],my_dict['awardedDate'],my_dict['description'],my_dict['start'],my_dict['end']))
    connection.commit()
    return count_rows


## Function to store the result of API in a table
def Func_Query_DB(res):
    rows= Func_Save_DB(res)
    DB_PATH = Func_Path_Set(config['SQLITE']['v_DBName'])
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        query=cursor.execute(config['SQLITE']['v_Query1'])
        q_res=query.fetchone()[0]
    return q_res
    
    
## Function to check status_code response from API
def Func_status(Opt,Res=""):
    if Res.status_code == 429:
       raise ApiError('Too many requests,retry after sometime {}'.format(Res.status_code))
    elif Res.status_code == 503:
       raise ApiError('Service Unavailable,retry after sometime {}'.format(Res.status_code))
    elif Res.status_code == 200:
       Func_Option(Opt,Res)
    else:
       raise ApiError('Some error has occurred {}'. format(Res.status_code))


## To call Functions based on user option from Menu
def Func_Option(Opt,Res=""): 
    if(Opt == 1):
        print('Response is Successfully fetched and is stored in {}'.format(Func_json_save(Res)))
    elif (Opt== 2):
        Start_date,End_date=Func_User_Input(Opt)
        print("Data between [{}] and [{}] is : {}".format(Start_date,End_date,Func_Search_btw_dates(Res,Start_date,End_date)))
    elif (Opt == 3):
        Description = Func_User_Input(Opt)
        print("Data matching [{}] is : {}".format(Description,Func_Search_desc(Res,Description)))  
    elif (Opt == 4):
        print("Data successfully loaded in Database, Records Added : {}".format(Func_Save_DB(Res)))
    elif (Opt== 5):
        print("Result of Query [{}] is : {}".format(config['SQLITE']['v_Query1'], Func_Query_DB(Res)))
    else:
        print("Invalid Option") ## This block will never execute


## Display Main Menu and take User Input
def Func_menu_option(options):
    print("MENU OPTIONS-")
    for serial in range(3):
        print(str(serial+1) + ":",options[serial])
    Sel_option = int(input("Enter a number: "))
    if Sel_option in range(1,4):
        return Sel_option
    else:
        print("Invalid Option")
        exit;


## Main Function
def main():
    if(len(sys.argv) > 1): ## Command Line Argument
        Sel_option = int(sys.argv[1])
    else:
        options=json.loads(config['MENU']['v_options'])
        Sel_option = Func_menu_option(options)
    
    Req_body = config['WEB']['v_Req_Body'] 
    Res = Func_POST_Notices(Req_body)
    Func_status(Sel_option,Res)


## Begin
if __name__  ==  "__main__":
    main()
