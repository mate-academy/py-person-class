
class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    person_list = []
    for man in people:
        person_list.append(Person(man["name"], man["age"]))

    for man in people:
        if "wife" in man and man["wife"] in Person.people:
            Person.people[man["name"]].wife = Person.people[man["wife"]]

        elif "husband" in man and man["husband"] in Person.people:
            Person.people[man["name"]].husband = Person.people[man["husband"]]

    return person_list


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]
""""
person_list = create_person_list(people)"""
person_list = Person.people
print(person_list)
