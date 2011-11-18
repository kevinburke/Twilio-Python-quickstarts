from flask import Flask, request
from twilio import twiml

app = Flask(__name__)

callers = {
    "+14158675309": "Curious George",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
    "+14158675312": "Marcel"
}

@app.route("/")
def hello_monkey():
    from_number = request.args.get('From', None)
    resp = twiml.Response()
    if from_number in callers:
        # Greet the caller by name
        resp.say("Hello " + callers[from_number])
    else:
        resp.say("Hello Monkey")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
