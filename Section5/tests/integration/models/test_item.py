from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context:
            StoreModel('test').save_to_db()
            item = ItemModel('test', 19.99, 1)

            self.assertIsNone(ItemModel.find_by_name('test'), f"Found an item with name {item.name}, but expected not to.")

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'))
            # It iss not none = it is exists.

            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name('test'))