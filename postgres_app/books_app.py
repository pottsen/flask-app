from flask import Flask, request

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Book

@app.get("/")
def hello():
    return "Hello World!"

@app.get("/name/<name>")
def get_book_name(name):
    return "name : {}".format(name)

@app.get("/details")
def get_book_details():
    author=request.args.get('author')
    published=request.args.get('published')
    return "Author : {}, Published: {}".format(author,published)

if __name__ == '__main__':
    app.run()
