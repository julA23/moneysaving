# FinCache
## _Elevate your fiscal fitness_
Introducing **FinCache** – your ultimate online money management platform. With its sleek interface and powerful features, FinCache offers an intuitive financial overview through interactive pie charts, providing instant insights into spending habits, income sources, and transfers. Dive deeper with detailed transaction tables, effortlessly sorting transactions by date, description, category, or type, ensuring meticulous recording and easy accessibility. With customizable categories and robust security measures, FinCache empowers users to achieve their financial goals while prioritizing privacy and data security. Experience the future of money management – sign up for FinCache today and take control of your finances like never before.
## Features
- **Financial Overview**:
Displays a pie chart providing a visual representation of the user's financial status.
Offers a comprehensive table summarizing transactions for a specified date range.
Includes columns for Date, Description, Category, and Transaction Type.
- **Transaction Management**:
Allows users to input transactions with details such as date, description, category, and transaction type.
Categories include Income, Expenses, and Transfer, with subcategories like Transport, Going Out, Health, etc.
Supports sorting transactions by category (Income, Expenses, Transfer) for easy analysis.
- **Income Tracking**:
Enables users to log their sources of income, providing insights into earnings over time.
Allows categorization of income sources for better organization and analysis.
- **Expense Tracking**:
Helps users monitor their spending habits by categorizing and tracking expenses.
Provides breakdowns of expenditures across different categories like groceries, holiday, education, etc.
Offers insights into where money is being spent excessively or efficiently.
- **Transfer Management**:
Facilitates tracking of transfers between accounts or individuals.
Allows users to categorize transfers and view them alongside other transactions.
Helps maintain a clear picture of funds moving within different accounts or entities.

## Tech

FinCache uses a number of open source projects to work properly:


- Django - High-level Python web framework that encourages rapid development and clean, pragmatic design.
- HTML - Standard markup language for creating web pages and web applications.
- CSS - Style sheet language used for describing the presentation of a document written in HTML.
- JavaScript - High-level, interpreted programming language that conforms to the ECMAScript specification.
- jsDelivr - Open-source CDN service to host and deliver web assets.

## Installation
### Step 1. Prerequisites
Make sure you have Python and pip installed on your system. You can download Python from [the official website](https://www.djangoproject.com/download/).
### Step 2. Clone Project Repository
Clone the project repository from your version control system (e.g., GitHub) or download the project source code as a ZIP archive and extract it to your desired location.
```sh
git clone https://github.com/julA23/moneysaving.git
cd <project_directory>
```
### Step 3. Setup Virtual Environment
Virtual environment setup can be done through the command below
```sh
pip install virtualenv
virtualenv venv
```
In order to activate it, you can go through the command below:
- On Windows
```sh
venv\Scripts\activate
```
- On macOS and Linux
```sh
source venv/bin/activate
```
### Step 4. Install Project Dependencies
Install the required Python packages specified in the `requirements.txt` file:
```sh
pip install -r requirements.txt
```
This will install the following libraries:
- `django`
- `gunicorn`
- `whitenoise`
- `psycopg2-binary`
- `requests`
- `urllib3`
- `django-environ`

### Step 5. Configure Environment Variable
If your project relies on environment variables for configuration (e.g., SECRET_KEY, DEBUG, database settings), create a .env file in the root directory of your project and add your environment variables there. Make sure not to include sensitive information in your code repository.

### Step 6. Running The Project
You can now run your Python project using the appropriate commands. For example, if you're using Django, you can start the development server:
```sh
python manage.py runserver
```
If you're using Gunicorn for production deployment, you can start the Gunicorn server:
```sh
gunicorn moneysaving.wsgi:application
```