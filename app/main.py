class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))
    for index, person in enumerate(people):
        if person.get("wife"):
            person_list[index].wife = Person.people[person["wife"]]
        elif person.get("husband"):
            person_list[index].husband = Person.people[person["husband"]]

    return person_list
