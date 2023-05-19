from flask import Flask, render_template, redirect, request
import uuid

app = Flask(__name__)

# Store the TODOLIST items
items = [
    {
        "id": "0",
        "title": "Example",
        "description": "This is an example todo-list item",
        "open": True,
    },
]


def gen_uuid():
    return uuid.uuid4()


@app.route("/")
def homepage():
    return render_template("index.html", items=items)


@app.route("/check/<id>", methods=["GET"])
def check_item(id):
    print(id)
    for item in items:
        if item["id"] == id:
            item["open"] = False
            break
    return redirect("/")


@app.route("/add", methods=["POST"])
def add_item():
    items.insert(0, {
        "id": str(gen_uuid()),
        "title": request.form["title"],
        "description": request.form["description"],
        "open": True,
    })
    return redirect("/")
