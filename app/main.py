class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(people)


def create_person_list(people: list) -> list:
    print([Person(current["name"], current["age"]) for current in people])
    return [Person(current["name"], current["age"]) for current in people]


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]
people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]

person_list = create_person_list(people)
