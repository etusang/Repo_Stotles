# Name

Tool to browse results from an external API

# Description

It's a command line menu driven project, which provides follwoing 3 options to users-
1. A user should be able to search for all notices (tenders and contracts) published between specified dates and browse the results.
2. The user should be able to narrow the results by performing text-search on the `description` field(case-insensitive substring match)
3. You can display the results in a simple list (stored in a file) [based on `noticeType` either `deadlineDate` (for tenders) and `awardedDate` (for awards) is displayed]

It also performs following 2 scheduled jobs-
1. Run on schedule time to fetch data from Contracts Finder API and store the notices in our DB.(sqlite3 DB)
2. Check the data against predefined search queries and "notify" the users if there are any matches (Ouput stored in a file)

Configuration File allows to setup following parameters-
1.Database Name
2.Search Query
3.URL
4.Request Body
5.Outfile Name
6.Menu Options


# Badges

#Menu Options
![Menu_Option](https://github.com/etusang/Repo1/blob/617c32f85a4d2c5895e09dbf791584b2e0065b23/1.Menu_Option.JPG?raw=true)

#CronTab
![Crontab](https://github.com/etusang/Repo1/blob/617c32f85a4d2c5895e09dbf791584b2e0065b23/2.Crontab.JPG?raw=true)

# Visuals

Menu Option1 -
![Menu_Option1](https://github.com/etusang/Repo1/blob/b8c60835ea4358c2399b4002db3a1c6fcece1a92/3.Menu_Option1.JPG?raw=true)

Menu Option2-
![Menu_Option2](https://github.com/etusang/Repo1/blob/140d974562b1f98020a8969ca255cd4dca48d068/4.Menu_Option2.JPG?raw=true)

Menu Option3-
![Menu_Option3](https://github.com/etusang/Repo1/blob/140d974562b1f98020a8969ca255cd4dca48d068/5.Menu_Option3.JPG?raw=true)

Crontab1-
![Crontab1](https://github.com/etusang/Repo1/blob/8664f521220c1db1777e1ff8efed2993eda8dfc4/6.Crontab1.JPG?raw=true)

CronTab2-
![Crontab2](https://github.com/etusang/Repo1/blob/8664f521220c1db1777e1ff8efed2993eda8dfc4/7.Crontab2.JPG?raw=true)

DB_Schema-
![DB_Schema](https://github.com/etusang/Repo1/blob/f78ff1ab3a5351407922d4a57ac9fb83953521cd/8.DB_schema.JPG?raw=true)

DB Table-
![DB_Table](https://github.com/etusang/Repo1/blob/8664f521220c1db1777e1ff8efed2993eda8dfc4/9.DB_Table_Value.JPG?raw=true)

# Installation

1. Python3
2. SQLite3


# Usage

Purpose of Each function-
  	def _url(path):
	## Setting URL
	
	Func_POST_Notices(task):
	##Post Notices
	
	Func_Path_Set(Name):
	## Setting Path from base directory
	
	Func_Parse_Notices(res):
	## Retrieving required fields from JSON response
	
	Func_json_save(resp):
	## To save the result of API in JSON format
	
	
	Func_User_Input(Opt):
	## User Input text for StartDate,EndDate and Description
	
	Func_Default_DB_val():
	## Setting Default Value for every row inserted in DB
	
	Func_Search_btw_dates(resp,start_date=0,end_date=0):
	## Search Notices between start date and end date
	
	Func_Search_desc(resp,desc=""):
	## Search Notices for description or part of description
	
	
	Func_create_table(cur):
	## Search Notices for description or part of description
	
	
	Func_Save_DB(resp):
	## Function to delete previous data and store the result of API in table
	
	
	Func_Query_DB(resp):
	## Function to store the result of API in a table
	
	
	Func_status(Res,Opt):
	## Function to check status_code response from API
	
	
	Func_Option(Res,Opt): 
	## To call Functions based on user option from Menu
	
	Func_menu_option(options):
	## Display Main Menu and take User Input
	
	Main
	## Main Function
	
	
## Order of Function Calls for each Option
	
	##Common for menu Driven Options
	Func_menu_option(options)
	Func_POST_Notices(task)
	Func_status(Res,Opt)
	Func_Option(Res,Opt)
	
	##Summary of Notices in a File
	Func_json_save(resp)
	Func_Parse_Notices(res)
	Func_Path_Set(Name)
	
	##Store Summary in Database
	Func_Save_DB(resp)
	Func_Parse_Notices(res)
	Func_Path_Set(Name)
	Func_Default_DB_val()
	Func_create_table(cur)
	
	##Search Notices by Description
	Func_Search_desc(resp,desc="")
	Func_Parse_Notices(res)
	
	##Search Notices Between Start and End Date
	Func_Search_btw_dates(resp,start_date=0,end_date=0):
	Func_Parse_Notices(res)
	
	##Search Notices from DB on Predefined Queries
	Func_Query_DB(resp) -> Func_Save_DB
	Func_Path_Set(Name)
	


# Support
Email: sangeetatulsiyan@gmail.com

# Roadmap
Exceptional Handling can be implemented
Users can be notified via email
Database column Mapping with JSON fields could be done separately
Output File Dictionary column Mapping with JSON fields could be done separately
Database can have primary key to avoid duplication of data (In this implementation Table content is deleted before inserting new Data)
Functions can be split into different files and import
Test Cases can be written
Configuration File Path can be picked from OS PATH
