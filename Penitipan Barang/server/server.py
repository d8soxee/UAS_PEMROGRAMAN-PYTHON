class StorageDatabase:
    def __init__(self):
        self.stored_items = []
        self.taken_items = []

    def add_item(self, item):
        self.stored_items.append(item)
        return item

    def take_item(self, item_id):
        for item in self.stored_items:
            if item['id'] == item_id:
                self.stored_items.remove(item)
                self.taken_items.append(item)
                return item
        return None

    def get_all_items(self):
        return self.stored_items

    def get_taken_items(self):
        return self.taken_items

    def update_item(self, item_id, new_data):
        for item in self.stored_items:
            if item['id'] == item_id:
                item.update(new_data)
                return item
        return None

    def delete_item(self, item_id):
        self.stored_items = [item for item in self.stored_items if item['id'] != item_id]
