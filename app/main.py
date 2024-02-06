class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        person_list.append(Person(person["name"], person["age"]))

    for person in people:
        person_instance = Person.people.get(person.get("name"))

        if person.get("wife") is not None:
            person_instance.wife = Person.people.get(person["wife"])

        if person.get("husband") is not None:
            person_instance.husband = Person.people.get(person["husband"])

    return person_list
