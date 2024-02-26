Fifithatlady Nanny Jobs Setup Instructions

Prerequisites
Before setting up Fifithatlady Nanny Jobs, ensure that you have the following installed:

Python 3.x
pip (Python package manager)

Installation
Clone the Fifithatlady Nanny Jobs repository from GitHub:

python3 -m venv venv

Activate the virtual environment:

On Windows:
venv\Scripts\activate

On macOS and Linux:
source venv/bin/activate

Install the required Python packages using pip:

pip install -r requirements.txt

Configuration
Create a .env file in the project root directory and define environment variables as needed. Example:

FLASK_ENV=development
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///fifithatlady_nanny_jobs.db

Update the database URL (DATABASE_URL) to point to your desired database. By default, it is configured to use SQLite.

Database Setup
Run the following commands to set up the initial database schema and populate it with sample data:

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

(Optional) If you want to populate the database with sample data, you can run:

flask db seed

Running the Application
Once everything is set up, you can start the Fifithatlady Nanny Jobs application by running:

flask run

By default, the application will run on http://127.0.0.1:5000/.

Testing
To run the unit tests, execute the following command:

python -m unittest discover tests/unit

To run the integration tests, execute the following command:

python -m unittest discover tests/integration

