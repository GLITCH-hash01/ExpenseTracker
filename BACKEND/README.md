# Backend API Documentation

Welcome to the documentation for the backend API of our expense tracking application. Below, you'll find detailed information about the API endpoints, their functionality, and how to use them.

## Requirements

- Django 4.2.4
- djangorestframework 3.14.0

## API Endpoints

### 1. Get Current Balance

- **URL:** `/get-balance/`
- **Method:** GET
- **Description:** Retrieve the current account balance.
- **Response:** Returns a JSON object with the latest record containing the current balance.

### 2. Add Expense

- **URL:** `/add-expense/`
- **Method:** POST
- **Description:** Add a new expense and keep track of it.
- **Request Body:** Requires a JSON object with the following fields:
  - `curnt_bal`: Indicates the current account balance after the expense.
  - `difference`: The difference between the previous balance and the new balance.
  - `reason`: A field for categorizing your expenses.
- **Response:** Returns a JSON object confirming the addition of the expense.

### 3. Get Expenses

- **URL:** `/get-expenses/`
- **Method:** GET
- **Description:** Get a list of all expenses with filtering options.
- **Query Parameters:** This endpoint supports various query parameters for filtering the returned expense list:
  - `date` (required): Specify the date in the format `dd`, `mm`, and `yy` (day, month, year).
  - `reason`: Filter expenses by category or a particular reason for the expense.
- **Response:** Returns a list of records containing all information regarding the expenses that match the specified criteria.

### 4. Total Expenses

- **URL:** `/total-expenses/`
- **Method:** GET
- **Description:** Calculate the total expenses within a specified date range.
- **Query Parameters:** This endpoint requires both `start` and `stop` query parameters, which should be strings containing dates in the format `YYYY-MM-DD`. These parameters help calculate the total expenses between the specified start and stop dates, inclusive.
- **Response:** Returns a JSON object containing the total expense within the specified date range.

## Future Plans

- Shifting to PostgreSQL: In the future, we plan to migrate our database to PostgreSQL for improved performance and scalability.

If you have any questions or need further assistance, please don't hesitate to contact us. Thank you for using our expense tracking application!
