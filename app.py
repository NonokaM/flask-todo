from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.sqlite'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

@app.route("/")
def index():
    message = "test_message = OK"

    todo_list = Todo.quary.all()
    print(todo_list)

    return render_template("base.html", message = message)

if __name__ == "__main__":
    db.create_all()

    new_todo = Todo(title="todo 1",compile=False)
    db.session.add(new_todo)
    db.session.commit()

    app.run(debug=True)


