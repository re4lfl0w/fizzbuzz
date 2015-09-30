# coding: utf-8
from flask import (Flask, request, jsonify)

from database import init_db
from database import db_session
from models import Cnt
from utils import fizz_buzz


app = Flask(__name__)


@app.route('/1/fizzbuzz/', methods=['GET', 'POST'])
def get_fizz_buzz():
    """
    Separate GET, POST behavior
    """
    if request.method == 'GET':
        cnt = db_session.query(Cnt).first()
        try:
            visit_cnt = cnt.visit_cnt
            result = fizz_buzz(visit_cnt)
        except Exception as e:
            print(e)
        return jsonify({'fizzbuzz': result})
    elif request.method == 'POST':
        cnt = db_session.query(Cnt).first()
        # Get visit_cnt from db
        visit_cnt = cnt.visit_cnt
        # Increase + 1 visit_cnt
        visit_cnt += 1
        cnt.visit_cnt = visit_cnt

        # Save db
        db_session.commit()

        result = fizz_buzz(visit_cnt)
        return jsonify({'fizzbuzz': result})


def init_cnt():
    """
    Initialize Cnt Table
    """
    cnt = Cnt(0)
    db_session.add(cnt)
    db_session.commit()


if __name__ == '__main__':
    init_db()
    init_cnt()
    app.run()
