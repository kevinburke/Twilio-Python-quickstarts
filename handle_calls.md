<link href="http://kevinburke.bitbucket.org/markdowncss/markdown.css" rel="stylesheet"></link>

## Handle Incoming Calls

### Before you start

This tutorial assumes you have a working Python development environment with
pip, virtualenv, Flask, and the twilio-python helper library. Please see your
post on [setting up your environment](#) if you need help installing those
programs.

To begin, you'll need a Twilio inbound phone number. You can use a [free Twilio
trial account](http://www.twilio.com/try-twilio) or upgrade your account and
get your own dedicated phone number.

### Sample App

Open a file called `run.py` and add the following lines:

##### run.py

    from flask import Flask
    import twilio

    app = Flask(__name__)

    @app.route("/")
    def hello_monkey():
        resp = twilio.twiml.Response()
        resp.say("Hello Monkey")

        return str(r)

    if __name__ == "__main__":
        app.run(debug=True)

Then run Flask:

    $ python run.py
    * Running on http://127.0.0.1:5000/ 

You should be able to open a web browser to `http://localhost:5000`. If you
view the page source code, you should see the following text:

    <?xml version="1.0" encoding="UTF-8"?><Response><Say>Hello Monkey</Say></Response>

#### Sharing your local server with Localtunnel 

You can access your localhost from your own computer, but for Twilio to be able
to read your TwiML, you need to put it at a public URL. We're going to use
a tool called [localtunnel](http://localtunnel.com), which allows you to share
your localhost with the world.

If you are on a Linux machine and don't have `rubygems` installed, run the
following command:

    $ sudo apt-get install ruby ruby1.8-dev rubygems1.8 libopenssl-ruby

Then, Mac and Linux users should run:

    $ sudo gem install localtunnel

Installing localtunnel on Windows is a bit more painful; there are instructions
[here](http://blog.wearemammoth.com/2011/09/localtunnel-windows.html). Windows
users may want to try using a public Dropbox folder, or [running Flask on
Heroku](http://devcenter.heroku.com/articles/python), for this part of the
tutorial.

Once you have localtunnel installed, open a new terminal window, and share your
local server with the world:

    $ localtunnel 5000
        This localtunnel service is brought to you by Twilio.
        Port 5000 is now publicly accessible from http://3fix.localtunnel.com ...

Your unique URL will probably be different. Copy
and paste the URL into the "Voice" URL on the
[Numbers](https://www.twilio.com/user/account/phone-numbers/incoming)
page of your Twilio Account. (If you are using a trial account,
copy and paste into the "Voice" URL in the Sandbox App part of your
[Dashboard](http://www.twilio.com/user/account)).

<img src="https://img.skitch.com/20111117-qch6mp7f5582s1wbnw139b9gf2.jpg"
alt="Twilio Numbers page" />

#### Try it out

Now call your Twilio number! You should hear a voice say "Hello Monkey" in
response. When you call, Twilio will fetch your URL, and execute the XML
instructions listed above. Then, Twilio will hang up, because there are no
more instructions.

#### Greet callers by name

Let's try to raise the stakes a bit. When someone calls, let's try to greet
them by name.

##### run.py

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

When Twilio makes a request to your URL, information about the call is included
along with the request, such as the number the call is coming from and the time
of the call. We then check to see if the caller is known looking up the number
in the `callers` dictionary to extract their name. We then Say their name, or
the word 'Monkey' if their Caller ID isn't known.

If you add your phone number and name to the `callers` dictionary, you can
listen to Twilio greet you by name. Note that the phone numbers in the
`callers` dictionary have +1 prepended to them. '1' is the international
country code for the US and Canada and the '+' formats the number in
[E.164](http://en.wikipedia.org/wiki/E.164) format which is used by Twilio when
passing you phone numbers.

<script src="http://yandex.st/highlightjs/6.1/highlight.min.js"></script>
<link href="http://softwaremaniacs.org/media/soft/highlight/styles/zenburn.css" rel="stylesheet" />
<script>hljs.initHighlightingOnLoad();</script>
