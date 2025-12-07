from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    name = request.args.get("name", "Suld")
    return render_template("index.html", name=name)


@app.route("/games")
def games():
    games = [
        {
            "title": "Maze Runner",
            "desc": "Navigate mazes and collect stars. Quick, fun levels.",
            "link": "#",
        },
        {
            "title": "Space Blaster",
            "desc": "Retro space shooter — dodge asteroids and blast aliens.",
            "link": "#",
        },
        {
            "title": "Puzzle Garden",
            "desc": "Relaxing match-and-grow puzzles to build a garden.",
            "link": "#",
        },
        {
            "title": "Platform Panic",
            "desc": "Action-packed platformer with tricky jumps and enemies.",
            "link": "/platformer",
        }
    ]
    return render_template("games.html", games=games)


@app.route("/platformer")
def platformer():
    return render_template("platformer.html")
from flask import Flask, request, render_template

# app = Flask(__name__)


# @app.route("/")
# def index():
#     name = request.args.get("name", "Suld")
#     return render_template("index.html", name=name)


# @app.route("/games")
# def games():
#     games = [
#         {
#             "title": "Maze Runner",
#             "desc": "Navigate mazes and collect stars. Quick, fun levels.",
#             "link": "#",
#         },
#         {
#             "title": "Space Blaster",
#             "desc": "Retro space shooter — dodge asteroids and blast aliens.",
#             "link": "#",
#         },
#         {
#             "title": "Puzzle Garden",
#             "desc": "Relaxing match-and-grow puzzles to build a garden.",
#             "link": "#",
#         },
#     ]
#     return render_template("games.html", games=games)
# from flask import Flask, request
# app = Flask(__name__)

# @app.route("/")
# def index():
#     name = request.args.get("name", "Suld")
#     return render_template("index.html", name=name)


# @app.route("/games")
# def games():
#     games = [
#         {
#             "title": "Maze Runner",
#             "desc": "Navigate mazes and collect stars. Quick, fun levels.",
#             "link": "#",
#         },
#         {
#             "title": "Space Blaster",
#             "desc": "Retro space shooter — dodge asteroids and blast aliens.",
#             "link": "#",
#         },
#         {
#             "title": "Puzzle Garden",
#             "desc": "Relaxing match-and-grow puzzles to build a garden.",
#             "link": "#",
#         },
#         {
#             "title": "Platform Panic",
#             "desc": "action-packed platformer with tricky jumps and enemies.",
#             "link": "/platformer",
#         }
#     ]
#     return render_template("games.html", games=games)
