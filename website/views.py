from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import ToDo

views = Blueprint("views", __name__)

# Index
@views.route("/")
def index():
    tasks = ToDo.query.all()
    return render_template("index.html", tasks=tasks)

# Add new task
@views.route("/add", methods=["POST"])
def add_task():
    task_name = request.form.get("new_task")
    if task_name:
        new_task = ToDo(name=task_name, complete=False)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for("views.index"))

# Update tasks
@views.route("/update", methods=["POST"])
def update_tasks():
    tasks = ToDo.query.all()
    for task in tasks:
        task.complete = bool(request.form.get(f"task_{task.id}"))
    db.session.commit()
    return redirect(url_for("views.index"))

# Delete tasks
@views.route("/delete/<int:task_id>")
def delete_task(task_id):
    task = ToDo.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("views.index"))