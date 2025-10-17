
Stage 0 – Dynamic Profile API (Cat Fact Generator and personal information)  This project is part of the HNG Internship Stage 0 Task, where we build a simple RESTful API endpoint that returns profile information along with a random cat fact fetched dynamically from an external API.

API ENDPOINT: method: GET , endpoint: /me , description: returns user details.
   example response: 

   {
  "status": "success",
  "user": {
    "email": "youremail@example.com",
    "name": "Your Full Name",
    "stack": "Python/Flask"
  },
  "timestamp": "2025-10-09T13:45:12.001Z",
  "fact": "Cats have five toes on their front paws, but only four on their back paws."
}


clone the repository at: git clone https://github.com/ABDULLATEEF18/stage0-catfact-api.git
cd stage0-catfact-api

create and activate virtual environment at: 
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows

install dependencies at:
pip install -r requirements.txt

run flask server at: 
flask --app app run

dependencies: 
Flask==3.0.3
requests==2.31.0


