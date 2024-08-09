class inventory:
    def __init__(self, item_image,):
        self.item_image = item_image
        item_list = []
        self.item = None

    def add_item(self, item):
        self.item_list.append(item)

    def remove_item(self, item):
        self.item_list.remove(item)