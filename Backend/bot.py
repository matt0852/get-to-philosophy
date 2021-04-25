from wiki_parser import get_all_links
from link_crawler import generate_links
import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods = ['GET'])
def return_links():
    if 'title' in request.args:
        title = request.args['title']
    else:
        return 'Bad request', 400

    return jsonify(
        title = title,
        links = generate_links(title))

app.run()