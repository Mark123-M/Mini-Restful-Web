Project Title: Mini RESTful Web Service Development (Group Member: Mark Joseph C Meraña)
Technology Used: PostMan and Python Flask
How to run the server locally (setup instructions):
Make Sure Flask is Installed(if not Installed :In your terminal, run: pip install flask)
Save the code in a file called app.py
Run the Server (Open a terminal then run : python app.py)
You should see output like this: Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
This means your local server is running. You can now:
Open a browser and go to http://localhost:5000/students to test GET.
Use Postman to test POST and other endpoints.
API endpoint descriptions:
GET /students
Description: Retrieves a list of all students
Sample JSON request body for POST:
{
  "name": "Charlie",
  "age": 23,
  "course": "Chemistry"
}
