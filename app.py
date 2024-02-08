from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        "author": 'nikhil',
        'title': 'my first post',
        'content': 'my first content',
        'Date_post': 'feb 08, 2024'

    },
    {
        "author2": 'gaurav',
        'title': 'my second post',
        'content': 'my second content',
        'Date_post': 'feb 09, 2024'
    }
]


@app.route("/",methods=['GET'])
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)