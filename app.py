from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def form():
    """Returns madlibs form with input forms for each prompt in story."""
    return render_template("questions.html", prompts=silly_story.prompts)
