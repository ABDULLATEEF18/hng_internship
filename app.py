from flask import Flask, jsonify

import requests

from datetime import datetime,  timezone

import os

app = Flask(__name__)


@app.route('/me', methods=['GET'])
def my_profilr():
    
      # get the current time
      current_time = datetime.now(timezone.utc).isoformat()
      # http for the cat fact
      cat_facts = "https://catfact.ninja/fact"
      # some error handling here
      try:
        response = requests.get(cat_facts, timeout=5)
        # raises errors for bad status codes.
        response.raise_for_status()  
        cat_fact = response.json().get("fact", "no available facts")
      except requests.exceptions.RequestException:
        # Handle network errors, timeouts, etc.
            cat_fact = "Could not fetch cat fact at this time."
      
      # data my endpoint is returning.
      
      my_data = {
       "status": "success",
       "user": {
       "email": "abdullateefatanda@student.oauife.edu.ng",
       "name": "Atanda Abdullateef",
       "stack": "python AND flask"
               },
        "timestamp": current_time,
        "fact": cat_fact
        }
      
      return jsonify(my_data), 200
if __name__ == "__main__":
   
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
