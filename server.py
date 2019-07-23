"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route("/")
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
        <head>
            <title>Home</title>
        </head>
        <body>
            Hi! This is the home page.
            <br>
            <a href="/hello">Hello!</a>
        </body>
    </html>"""


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
            What's your name? <input type="text" name="person">
            <br>
            Choose a compliment:
            <select name="compliment">
                <option>Pretty</option>
                <option>Smart</option>
                <option>Awesome</option>
                <option>Badass</option>
            </select>
            <br>
            <input type="submit" value="Submit">
        </form>
        <form action="/diss">
            <input type="submit" value="Insult me instead!">
        </form>
      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get('compliment')

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


@app.route("/diss")
def diss_person():
    """Insult the user."""

    player = request.args.get("person")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi, brat! I think you're scum!
      </body>
    </html>
    """



if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
