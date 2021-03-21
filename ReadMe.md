# Name
Tool to browse results from an external API

# Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

It's a command line menu driven project, which provides follwoing 5 options to users-
1. A user should be able to search for all notices (tenders and contracts) published between specified dates and browse the results.
2. The user should be able to narrow the results by performing text-search on the `description` field.(case-insensitive substring match)
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
Menu Options
Image

#CronTab
Image

#Flow
Image


# Visuals
Menu Option1 -
![Menu_Option1](https://github.com/etusang/Repo1/blob/140d974562b1f98020a8969ca255cd4dca48d068/3.Menu_Option1.JPG?raw=true)

Menu Option2-
![Menu_Option1](https://github.com/etusang/Repo1/blob/140d974562b1f98020a8969ca255cd4dca48d068/4.Menu_Option2.JPG?raw=true)

Menu Option3-
![Menu_Option1](https://github.com/etusang/Repo1/blob/140d974562b1f98020a8969ca255cd4dca48d068/5.Menu_Option3.JPG?raw=true)

Crontab1-

CronTab2-

DB_Schema-


# Installation
1. Python3
2. SQLite3


# Usage


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

# Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

# Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

# License
For open source projects, say how it is licensed.

# Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
