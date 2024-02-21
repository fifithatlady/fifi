QuickSearch Estates Setup Instructions
Prerequisites
Before setting up QuickSearch Estates, ensure that you have the following installed:

Python 3.x
pip (Python package manager)
Installation
Clone the QuickSearch Estates repository from GitHub:

Copy code
python3 -m venv venv
Activate the virtual environment:

On Windows:
bash
Copy code
venv\Scripts\activate
On macOS and Linux:
bash
Copy code
source venv/bin/activate
Install the required Python packages using pip:

bash
Copy code
pip install -r requirements.txt
Configuration
Create a .env file in the project root directory and define environment variables as needed. Example:

dotenv
Copy code
FLASK_ENV=development
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///quicksearch_estates.db
Update the database URL (DATABASE_URL) to point to your desired database. By default, it is configured to use SQLite.

Database Setup
Run the following commands to set up the initial database schema and populate it with sample data:

bash
Copy code
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
(Optional) If you want to populate the database with sample data, you can run:

bash
Copy code
flask db seed
Running the Application
Once everything is set up, you can start the QuickSearch Estates application by running:

bash
Copy code
flask run
By default, the application will run on http://127.0.0.1:5000/.

Testing
To run the unit tests, execute the following command:

bash
Copy code
python -m unittest discover tests/unit
To run the integration tests, execute the following command:

bash
Copy code
python -m unittest discover tests/integration
