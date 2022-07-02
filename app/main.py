class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

        Person.people.update({
            name: self
        })


def create_person_list(people: list) -> list:
    person_list = [Person(i["name"], i["age"]) for i in people]
    return person_list



