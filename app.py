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


@app.get("/results")
def return_result():
    """Returns the final text with the user's inputs"""

# TODO: pass request.args
    text = silly_story.get_result_text(
        {item: request.args[item] for item in silly_story.prompts})
# TODO: name text as result
    return render_template('results.html', result=text)
