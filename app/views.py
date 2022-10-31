from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

count = 0
@app.route("/counter")
def counter():
    global count
    count += 1
    return str(count)