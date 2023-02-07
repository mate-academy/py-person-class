class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_ = list()
    for person in people:
        list_.append(Person(person["name"], person["age"]))

    for index, person in enumerate(people):
        if person.get("wife"):
            list_[index].wife = Person.people.get(person.get("wife"))
        else:
            list_[index].husband = Person.people.get(person.get("husband"))

    return list_
