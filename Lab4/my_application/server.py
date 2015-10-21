from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/")
def index():
	return "Index File"

@app.route("/user/<username>")
def show_username(username):
	return "User %s" % username

@app.route("/post/<int:post_id>")
def post(post_id):
	return "Post %d" % post_id



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)
