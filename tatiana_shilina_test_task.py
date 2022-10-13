# Тестовое задание для ООО "СТАТУС" на вакансию Разработчик (Backend developer / Python)
# Шилина Татьяна


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]


class TreeStore:

    def __init__(self, items: list):
        self.items = items

    def getAll(self):
        print(self.items)

    def getItem(self, the_id):
        for item in self.items:
            if item['id'] == the_id:
                print(item)

    def getChildren(self, the_id):
        myarray = []
        for item in self.items:
            if item['parent'] == the_id:
                myarray.append(item)
        print(myarray)

    def getAllParents(self, the_id):
        myarray = []
        for item in self.items:
            if item['id'] == the_id:
                index = self.items.index(item)
        for item in self.items[:index]:
            myarray.append(item)
        myarray = myarray[::-1]
        print(myarray)






ts = TreeStore(items)
ts.getAllParents(3)
