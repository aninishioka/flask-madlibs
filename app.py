from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

STORIES = {1: silly_story, 2: excited_story}

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def story_menu():
    return render_template("story_menu.html", stories=STORIES)

@app.get('/<template>')
def form():
    """Returns madlibs form with input forms for each prompt in story."""
    return render_template("questions.html", prompts=silly_story.prompts)


@app.get("/results")
def return_result():
    """Returns the final text with the user's inputs"""

    result = silly_story.get_result_text(request.args)
    return render_template('results.html', result=result)
