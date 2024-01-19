#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, session
from flask_migrate import Migrate

from models import db, Article, User

app = Flask(__name__)
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/clear')
def clear_session():
    session['page_views'] = 0
    return {'message': '200: Successfully cleared session data.'}, 200

@app.route('/articles',methods=['GET'])
def index_articles():

    pass

@app.route('/articles/<int:id>',methods=['GET'])
def show_article(id):
    if 'page_views' not in session:
      session['page_views'] =0

    # Increment the 'page_views' by 1 for each request.
    session['page_views'] += 1

    # Check if the user has viewed more than 3 pages.
    if session['page_views'] > 3:
        # Render a JSON response with an error message and status code 401.
        return jsonify({'message': 'Maximum pageview limit reached'}), 401
     
    article_data = {
        'author': 'john',
        'title': 'Sample Article',
        'content': 'This is a sample article content.',
        'preview': 'This is a preview of the article.',
        'minutes_to_read':'20',
        'date':'12/03/2020'
    }

    return make_response(jsonify(article_data), 200)
if __name__ == '__main__':
    app.run(port=5555)