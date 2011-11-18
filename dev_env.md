<link href="http://kevinburke.bitbucket.org/markdowncss/markdown.css" rel="stylesheet"></link>

## Setting up a Local Dev Environment

To complete the Twilio Python quickstart, you'll need to have the following
tools installed:

* Python
* Flask
* The twilio-python library
* Localtunnel

### Installing Python

If you are on a Mac or Linux machine, you probably already have
Python installed. Windows users can follow this [excellent
tutorial](http://www.richarddooling.com/index.php/2006/03/14/python-on-xp-7-minutes-to-hello-world/ 
"Python installation tutorial"). There are more advanced
configuration instructions at the [official Python
website](http://docs.python.org/using/index.html).

### Installing Flask and twilio-python

[Flask](http://flask.pocoo.org/) is a simple web server written in Python. To
install it, we are going to install two tools: `pip` and `virtualenv`. `pip`
is a package manager that you can use to install new Python libraries with one
command. `virtualenv` is a tool that lets you create a special sandbox for
your Python packages, to ensure that you have exactly the right version of
every tool you need, and that you don't accidentally break your app if someone
updates your packages.

The good news is that `pip` comes installed with `virtualenv`. Open a terminal
and run the following command:

    $ easy_install virtualenv

If you get the following error:

    -bash: easy_install: command not found

you may need to ensure that Python is installed, or add the folder containing
the `easy_install` program to your `$PATH`.

Once you have `virtualenv` installed, set up a virtualenv:

    $ virtualenv --no-site-packages .

Now activate the virtual environment:

    $ source bin/activate

You must activate the virtual environment every time you use your Python app.
You can tell it is running, because your terminal will have the name of the
enclosing folder listed above it:

    (quickstart)
    $

Now we're going to install Flask and the twilio-python library. Open a file
called `requirements.txt` and add the following lines to it:

##### requirements.txt

    Flask==0.8
    twilio=3.3.3

Then install these packages with `pip`:

    $ bin/pip install -r requirements.txt

Congrats, you now have everything you need to start using Twilio and Python!

<script src="http://yandex.st/highlightjs/6.1/highlight.min.js"></script>
<link href="http://softwaremaniacs.org/media/soft/highlight/styles/zenburn.css" rel="stylesheet" />
<script>hljs.initHighlightingOnLoad();</script>
