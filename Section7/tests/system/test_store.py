from models.store import StoreModel
from models.item import ItemModel
from tests.base_test import BaseTest
import json


class StoreTest(BaseTest):
    def test_create_store(self):
        store_name = 'test'

        with self.app() as client:
            with self.app_context:
                response = client.post(
                    f'/store/{store_name}'
                )

                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(StoreModel.find_by_name(store_name))
                self.assertDictEqual(
                    {'name': store_name,
                     'items': []
                     }, json.loads(response.data)
                )

    def test_create_duplicate_store(self):
        store_name = 'test'

        with self.app() as client:
            with self.app_context:
                client.post(
                    f'/store/{store_name}'
                )

                response = client.post(
                    f'/store/{store_name}'
                )

                self.assertEqual(response.status_code, 400)

    def test_delete_store(self):
        store_name = 'test'

        with self.app() as client:
            with self.app_context:
                client.post(
                    f'/store/{store_name}'
                )

                response = client.delete(
                    f'/store/{store_name}'
                )

                self.assertEqual(response.status_code, 200)
                self.assertEqual(
                    'store deleted',
                    json.loads(response.data)['message']
                )

    def test_find_store(self):
        store_name = 'test'

        with self.app() as client:
            with self.app_context:
                client.post(
                    f'/store/{store_name}'
                )

                response = client.get(f'/store/{store_name}')

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual(
                    {'name': store_name,
                     'items': []
                     }, json.loads(response.data)
                )

    def test_store_not_found(self):
        store_name = 'test'

        with self.app() as client:
            with self.app_context:
                response = client.get(f'/store/{store_name}')

                self.assertEqual(response.status_code, 404)
                self.assertEqual(
                    'store not found',
                    json.loads(response.data)['message']
                )


    def test_store_found_with_items(self):
        store_name = 'test'

        with self.app() as client:
            with self.app_context:
                client.post(
                    f'/store/{store_name}'
                )
                ItemModel('test', 19.99, 1).save_to_db()

                response = client.get(f'/store/{store_name}')

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual(
                    {'name': store_name,
                     'items': [{
                         'name':'test',
                         'price':19.99
                        }]
                     },
                    json.loads(response.data)
                )


    def test_store_list(self):
        store_name = 'test'

        with self.app() as client:
            with self.app_context:
                client.post(
                    f'/store/{store_name}'
                )

                response = client.get('/stores')

                self.assertDictEqual(
                    {
                        'stores': [
                            {
                                'name':'test',
                                'items':[]
                            }
                        ]
                    },
                    json.loads(response.data)
                )



    def test_store_list_with_items(self):
        store_name = 'test'

        with self.app() as client:
            with self.app_context:
                client.post(
                    f'/store/{store_name}'
                )
                ItemModel('test', 19.99, 1).save_to_db()

                response = client.get('/stores')

                self.assertDictEqual(
                    {
                        'stores': [
                            {
                                'name': 'test',
                                'items': [
                                    {
                                        'name':'test',
                                        'price':19.99
                                    }
                                ]
                            }
                        ]
                    },
                    json.loads(response.data)
                )
