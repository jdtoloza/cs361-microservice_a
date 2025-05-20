## Summary ##

Calculation Microservice – Mean, Median, Mode

This microservice accepts a list of numbers and a mode type (`mean`, `median`, or `mode`) and returns the calculated result.

## REQUEST Instructions ##

Make a **POST** request to the following endpoint: POST http://localhost:3000/calculate
-- Headers --
Content-Type: application/json

-- Body --
{
  "numbers": [1, 2, 2, 3, 4],
  "mode": "mode"
}

JSON Response Example:
{
  "numbers": [1, 2, 2, 3, 4],
  "mode": "mode",
  "result": 2
}

Error Response Example:
{
  "numbers": [1, 2, 3],
  "mode": "average",
  "error": "Invalid mode type. Please use mean, median, or mode."
}

## Mitigation Plan ##
Who is this microservice for?
I implemented Microservice A for Yao-You Chang

What is the current status of the microservice?
Complete and tested. Fully operational.

How should your teammate access the microservice?
Clone the repo from GitHub: https://github.com/jdtoloza/cs361-microservice_a

Run it locally using Python and Flask.

If your teammate cannot access/call your microservice, what should they do?
Ensure you have the proper packages installed for python environment. Flask, flask-cors, requests. If that doesn't work, contact me directly email or microsoft teams. 

By when do they need to tell you if there’s an issue?
Please notify me by Friday, May 28th at 5:00 PM PDT so I can assist before final integration.

Additional Notes
Input must be a list of numbers (e.g. [1, 2, 3])

Mode types must be one of: mean, median, mode (case-insensitive).

This service uses Python 3.10+ for match-case. 
