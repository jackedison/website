import unittest
from my_package import app, db
from my_package.models import User, Post


class UserModelCase(unittest.TestCase):
    # Special method set up before each test
    # This swaps to an in memory SQLite database to not mess up our own
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()  # Create all db tables in our mock db

    # Special method ran after each test
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_pwd_hash(self):
        u = User(username='temp')
        u.set_password('foobar')
        self.assertTrue(u.check_password('foobar'))
        self.assertFalse(u.check_password('frodo'))

    def test_avatar(self):
        u = User(username='temp2', email='temp2@hotmail.com')
        self.assertEqual(u.avatar(128), ('https://www.gravatar.com/avatar/'
                                         'c433b182f1946468e994e8fc5d02be2e'
                                         '?d=identicon&s=128'))


if __name__ == '__main__':
    unittest.main(verbosity=2)  # Verbosity gives extra detail (0, 1, or 2)
