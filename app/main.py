class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    list_ = list()
    for person in people:
        list_.append(Person(person["name"], person["age"]))
        Person.people[person["name"]] = list_[-1]
    for i, person in enumerate(people):
        if person.get("wife"):
            list_[i].wife = Person.people.get(person.get("wife"))
        else:
            list_[i].husband = Person.people.get(person.get("husband"))

    return list_
