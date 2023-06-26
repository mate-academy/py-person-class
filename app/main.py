class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = list()
    for person in people:
        person_list.append(Person(person["name"], person["age"]))

    for person in people:
        if person.get("wife"):
            Person.people.get(
                person["name"]
            ).wife = Person.people.get(person["wife"])
        if person.get("husband"):
            Person.people.get(
                person["name"]
            ).husband = Person.people.get(person["husband"])

    return person_list
