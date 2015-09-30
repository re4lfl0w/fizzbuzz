import os
import unittest
import tempfile

from flask_simple import init_cnt
import flask_simple


class FizzBuzzTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, flask_simple.app.config['DATABASE'] = tempfile.mkstemp()
        flask_simple.app.config['TESTING'] = True
        self.app = flask_simple.app.test_client()
        flask_simple.init_db()
        init_cnt()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flask_simple.app.config['DATABASE'])
        os.remove('./flask_simple.db')

    def test_zero_visit(self):
        rv = self.app.get('/1/fizzbuzz/')
        assert '0' in rv.data

    def test_three_times_visit(self):
        for i in range(3):
            rv = self.app.post('/1/fizzbuzz/')
        assert 'Fizz' in rv.data

    def test_five_times_visit(self):
        for i in range(5):
            rv = self.app.post('/1/fizzbuzz/')
        assert 'Buzz' in rv.data

    def test_fifteen_times_visit(self):
        for i in range(15):
            rv = self.app.post('/1/fizzbuzz/')
        assert 'FizzBuzz' in rv.data

    def test_sixteen_times_visit(self):
        for i in range(16):
            rv = self.app.post('/1/fizzbuzz/')
        assert '16' in rv.data

    def test_a_hundred_times_visit(self):
        for i in range(100):
            rv = self.app.post('/1/fizzbuzz/')
        assert 'Buzz' in rv.data


if __name__ == '__main__':
    unittest.main()