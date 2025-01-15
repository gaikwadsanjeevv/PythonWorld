# Personal Expense Tracker API
To run the zip project file, click[RunSteps.md](RunSteps.md)    #ctrl + click the name of file inside()

For details of project Development steps go down 


## Overview
This project is a RESTful API built using Flask and SQLite to manage and analyze personal expenses. Users can perform CRUD operations on expenses and access analytics endpoints for summaries and insights.

---

## Features
- **Create Expense**: Add new expenses with details like amount, description, category, and date.
- **Fetch Expenses**: Retrieve all expenses or specific ones using filters.
- **Update Expense**: Modify details of existing expenses.
- **Delete Expense**: Remove expenses by ID.
- **Analytics**:
  - Total expenses and category breakdown.
  - Highest single expense.
  - Monthly summary for a given year.

---

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- SQLite installed
- Flask installed

#### Verify Installation: on Terminal
python --version
python -m ensurepip --upgrade

### Steps to Set Up

   ## Install Dependencies:  
pip install -r requirements.txt
pip install flask flask-sqlalchemy

## Create Folder Structure: 

expense_tracker/  
|----- app/  
|        |-----  _init_.py  
|        |-----models.py    
|        |-----routes.py 
|----- tests/  
|-----requirements.txt  
|-----app.py  
|___ README.md  

## Set up Virtual Environment  - in Terminal  
python -m venv expense_tracker_env  
On Windows: expense_tracker_env\Scripts\activate  

cd .\expense_tracker\  //as app.py is in folder expense_tracker and now we can run the app as below


## Initializa Database:  
python app.py  
This will create expense_tracker.db in the instance folder.  

The app will run locally on http://127.0.0.1:5000.  

-------------------------------------------------------------------------------  
# API Documentation  
For detailed API information, refer to [API.md](API.md).

--------------------------------------------------------------------------------  
# Challenges and Solutions
For detailed Challenges faced and solution, refer to[challenges.md](challenges.md)
