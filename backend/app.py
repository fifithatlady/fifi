from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Dummy data for testing purposes
nanny_jobs = [
    {
        "id": 1,
        "title": "Full-Time Nanny",
        "description": "Looking for a full-time nanny to take care of two children.",
        "location": "Cape Town, South Africa",
        "salary": "$2000 per month",
        "requirements": ["Experience with infants", "First aid certification"],
        "contact": "example@example.com"
    },
    {
        "id": 2,
        "title": "Part-Time Nanny",
        "description": "Seeking a part-time nanny for after-school care.",
        "location": "Johannesburg, South Africa",
        "salary": "$15 per hour",
        "requirements": ["Valid driver's license", "CPR training"],
        "contact": "info@example.com"
    },
    {
        "id": 3,
        "title": "Live-In Nanny",
        "description": "Family seeking a live-in nanny for childcare and light housekeeping.",
        "location": "Durban, South Africa",
        "salary": "Negotiable",
        "requirements": ["Fluency in English", "Ability to cook meals"],
        "contact": "contact@example.com"
    }
]

@app.route('/api/nanny_jobs/search', methods=['POST'])
def search_nanny_jobs():
    search_query = request.form.get('searchQuery')
    # Perform search logic based on search_query
    # For demonstration, just filter nanny jobs by location
    filtered_jobs = [job for job in nanny_jobs if job['location'] == search_query]
    return jsonify(filtered_jobs)

@app.route('/api/data')
def get_data():
    # Perform some operation to retrieve data
    data = {'key': 'value'}
    return jsonify(data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

