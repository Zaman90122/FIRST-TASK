from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

 
def init_db():
    conn = sqlite3.connect("tasks.db")
    conn.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT, done INTEGER)")
    conn.close()
init_db()

@app.route('/')
def index():
    conn = sqlite3.connect("tasks.db")
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return render_template("index.html", tasks=tasks)
init_db

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    conn = sqlite3.connect("tasks.db")
    conn.execute("INSERT INTO tasks (task, done) VALUES (?,0)", (task,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/done/<int:id>')
def done(id):
    conn = sqlite3.connect("tasks.db")
    conn.execute("UPDATE tasks SET done=1 WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect("tasks.db")
    conn.execute("DELETE FROM tasks WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5001)