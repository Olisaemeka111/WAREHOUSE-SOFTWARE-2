# Placeholder for business logic related to items
import unittest
from app import app, db
from models import Item

class ItemTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_item(self):
        response = self.app.post('/items', json={
            'barcode': '123456',
            'name': 'Test Item',
            'weight': 10.5,
            'size': 'M',
            'received_at': '2023-01-01T00:00:00'
        })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
