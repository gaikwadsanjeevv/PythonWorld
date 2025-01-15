# API Documentation  
## CRUD Operations 

## Testing with Postman
URL: https://www.postman.com/
Note: while testing an API Locally we need to use the Postman Desktop agent so download and install it.
Import the API endpoints into Postman for easy testing.
Use the provided request and response examples as below to set up and verify each endpoint.

### POST /expenses  
Description: Create a new expense.  
Request: 
Method: POST  
URL: http://127.0.0.1:5000/expenses
JSON:  
{  
  "amount": 50.5,  
  "description": "Groceries",  
  "category": "Food",  
  "date": "2024-12-23T12:00:00"  
}  
Response:  
{  
  "message": "Expense created!",  
  "id": 1  
}  

### GET /expenses  
Description: Fetch all expenses.  
Request: 
Method: GET
URL: http://127.0.0.1:5000/expenses
JSON:
  [
    {
        "amount": 50.5,
        "category": "Food",
        "date": "2024-12-23T12:00:00",
        "description": "Groceries",
        "id": 2
    },
    {
        "amount": 120.75,
        "category": "Utilities",
        "date": "2024-12-01T10:00:00",
        "description": "Monthly electricity bill",
        "id": 3
    },
    {
        "amount": 45.5,
        "category": "Food",
        "date": "2024-12-15T19:30:00",
        "description": "Dinner at a restaurant",
        "id": 4
    },
    {
        "amount": 15.0,
        "category": "Transport",
        "date": "2024-12-18T08:15:00",
        "description": "Bus fare for commute",
        "id": 5
    },
    {
        "amount": 250.0,
        "category": "Shopping",
        "date": "2024-12-20T14:45:00",
        "description": "Clothing and accessories shopping",
        "id": 6
    },
    {
        "amount": 30.0,
        "category": "Entertainment",
        "date": "2024-12-21T20:00:00",
        "description": "Movie tickets for two",
        "id": 7
    },
    {
        "amount": 40.0,
        "category": "Fitness",
        "date": "2024-12-01T07:00:00",
        "description": "Monthly gym membership fee",
        "id": 8
    },
    {
        "amount": 65.3,
        "category": "Transport",
        "date": "2024-12-22T11:00:00",
        "description": "Gasoline refill for the car",
        "id": 9
    },
    {
        "amount": 55.0,
        "category": "Utilities",
        "date": "2024-12-05T09:00:00",
        "description": "Monthly internet service",
        "id": 10
    },
    {
        "amount": 85.0,
        "category": "Education",
        "date": "2024-12-10T15:00:00",
        "description": "Educational books and materials",
        "id": 11
    },
    {
        "amount": 100.0,
        "category": "Charity",
        "date": "2024-12-25T10:30:00",
        "description": "Donation to a local charity",
        "id": 12
    }
]

### PUT /expenses/<id=1>  
Description: Update an expense by ID.
Request: 
Method: PUT
URL:   http://127.0.0.1:5000/expenses/1

JSON: 
{
  "amount": 60.0,
  "description": "Updated Groceries"
}
Response:  
{
  "message": "Expense updated!"
}

### DELETE /expenses/<id>
Description: Delete an expense by ID.  
Request: 
Method: DELETE  
URL: http://127.0.0.1:5000/expenses/1
Response:  
{
  "message": "Expense deleted!"
}

---------------------------------------------------------------------  
## Analytics Endpoints  

### GET /summary  
Request: 
Method: GET  
URL: http://127.0.0.1:5000/summary  
Response: 
{
    "category_breakdown": {
        "Charity": 100.0,
        "Education": 85.0,
        "Entertainment": 30.0,
        "Fitness": 40.0,
        "Food": 96.0,
        "Shopping": 250.0,
        "Transport": 80.3,
        "Utilities": 175.75
    },
    "total_expenses": 857.05
}

### GET /highest-expense
Request: 
Method: GET  
URL: http://127.0.0.1:5000/highest-expense
Response: 
{
    "amount": 250.0,
    "category": "Shopping",
    "date": "2024-12-20T14:45:00",
    "description": "Clothing and accessories shopping",
    "id": 6
}

### GET /monthly-summary/<year>
Request:
Method: GET
URL: http://127.0.0.1:5000/monthly-summary/2024
Response: 
{
    "monthly_summary": {
        "12": 857.05
    },
    "year": 2024
}
Go Back to [README.md](README.md).