class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for i in people:
        person = Person(i["name"], i["age"])
        person_list.append(person)

    for i in people:
        person = Person.people[i["name"]]
        if "wife" in i and i["wife"]:
            person.wife = Person.people[i["wife"]]
        if "husband" in i and i["husband"]:
            person.husband = Person.people[i["husband"]]

    return person_list
