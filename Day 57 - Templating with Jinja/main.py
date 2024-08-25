import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    api_url = "https://api.npoint.io/c790b4d5cab58020d391"

    posts = requests.get(api_url).json()

    return render_template("index.html", posts=posts)


@app.route('/post/<int:post_id>')
def get_post(post_id):
    api_url = "https://api.npoint.io/c790b4d5cab58020d391"
    posts = requests.get(api_url).json()

    post = posts[post_id - 1]

    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
