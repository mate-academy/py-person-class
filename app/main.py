class Person:

    people = [
        {"name": "Ross", "age": 30, "husband": "Rachel"},
        {"name": "Joey", "age": 29, "husband": None},
        {"name": "Rachel", "age": 28, "husband": "Ross"}
    ]

    husband = None
    wife = None

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def create_person_list(self):
        return [Person(i["name"], i["age"])
                for i in Person.people]

