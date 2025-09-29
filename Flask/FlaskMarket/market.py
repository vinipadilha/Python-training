from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hello, World 1!'

@app.route("/about/<username>")
def about_page(username):   
    return f'About {username}'


if __name__ == "__main__":
    app.run(debug=True, port=5001)

