# coding: utf-8
from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Cnt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    visit_cnt = db.Column(db.Integer)

    def __repr__(self):
        return '%d' % self.visit_cnt


def fizz_buzz(visit_cnt):
    if visit_cnt % 15 == 0:
        return 'FizzBuzz'
    elif visit_cnt % 5 == 0:
        return 'Buzz'
    elif visit_cnt % 3 == 0:
        return 'Fizz'
    else:
        return visit_cnt

@app.route('/1/fizzbuzz/', methods=['GET'])
def get_fizz_buzz():
    cnt = Cnt()
    visit_cnt = cnt.visit_cnt
    print(visit_cnt)
    result = fizz_buzz(visit_cnt)
    return jsonify({'fizzbuzz': result})


@app.route('/1/fizzbuzz/', methods=['POST'])
def post_fizz_buzz():
    cnt = Cnt()
    # Get visit_cnt from db
    visit_cnt = cnt.visit_cnt
    # Increase + 1 visit_cnt
    visit_cnt += 1
    cnt.visit_cnt = visit_cnt

    # Save db
    db.session.commit()

    result = fizz_buzz(visit_cnt)
    return jsonify({'fizzbuzz': result})


if __name__ == '__main__':
    app.run()
