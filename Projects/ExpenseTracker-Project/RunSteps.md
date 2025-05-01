Steps to run the project :  
 Note below # represents the comments.

1. Download project from drive and extract the zip on local pc  
            > Open the visual studio code and open the project there.

2. Install python latest version (https://www.python.org/ftp/python/3.13.1/python-3.13.1-amd64.exe)
3. verify installation on terminal : 
             >   python --version   # click Add python.exe to PATH during installation
             >  python -m ensurepip --upgrade  #installing or upgrading pip
             >  pip install flask flask-sqlalchemy  #Install Flask and SQLite3 libraries:

4.  
5. Open terminal on VS Code and activate the environment by below code: 
               > expense_tracker_env\Scripts\activate      #we can see an circle before the project link.

6. The environment is setup now move into folder where we have app.py the entry point of project and run
                > cd expense_tracker
                > python app.py

                You should see a message like:
                    * Running on http://127.0.0.1:5000/         # The project is running successfully

GO to any browser and paste : http://127.0.0.1:5000/expenses     # to see all expenses of the table

7. Now lets check for different API request go to: [API.md](API.md)
and test various request through API methods on postman.

                > visit https://www.postman.com/   click new Request
** Note: while testing an API Locally we need to use the Postman Desktop agent so download and install it.
                > select a API method to verify and get the correct data, for sample json data check API.md
                > The API.md has for methods GET, PUT, POST, DELETE methods
                > The API.md has also for Analytics summary methods to retive data.

8. Install SQLite on your system to use the CLI of SQLite
https://www.sqlite.org/2024/sqlite-tools-win-x64-3470200.zip

 >  sqlite3 --version  # on terminal

> cd D:\coding\roseai\expense_tracker\instance  # navigate to folder containing expense_tracker.db
> sqlite3 expense_tracker.db

 Now use different SQL commands to inspect the database: This step is an important step to ensure the correctness of your analytical endpoints and validate that the API is working as intended.

Following are some of SQL commands to verify the API logic is working correctly: 
> .tables   #list all tables
> SELECT * FROM Expense;  #view all data in expense table
> SELECT SUM(amount) AS total_expenses FROM Expense;   #Summary total expense
> SELECT category, SUM(amount) AS total_by_category FROM Expense GROUP BY category;
> SELECT * FROM Expense ORDER BY amount DESC LIMIT 1;
> .exit

Go back to Main README for more details[README.md](README.md)



















Go Back to [README.md](README.md).