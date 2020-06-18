from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)

app.config['SECRET_KEY']="oh-so-secret"
debug = DebugToolbarExtension(app)

@app.route("/")
def home_page():

    return render_template("home.html", )

@app.route("/form")
def form():
    story_choice = request.args["story_choice"]
    story = stories[story_choice]
    title = story.title
    prompts = story.prompts
    return render_template("form.html", title=title, prompts=prompts, story_choice=story_choice)

@app.route("/story")
def present_story():
    story_choice = request.args["story_choice"]
    story = stories[story_choice]
    final_story = story.generate(request.args)
    return render_template("story.html", final_story=final_story)