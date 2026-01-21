class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:

    list_of_people = []

    for person in people:
        list_of_people.append(Person(person["name"], person["age"]))

    for person in people:
        if "wife" in person and person["wife"] is not None:
            Person.people[person["name"]].wife \
                = (Person.people.get(person["wife"]))
        elif "husband" in person and person["husband"] is not None:
            Person.people[person["name"]].husband \
                = Person.people.get(person["husband"])

    return list_of_people
