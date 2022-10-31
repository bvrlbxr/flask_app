from app import app



@app.route("/")
def main():
    return "hello"

count = 0
@app.route("/counter")
def counter():
    global count
    count += 1
    return str(count)