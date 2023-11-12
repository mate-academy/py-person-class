class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_data in people:
        name = person_data["name"]
        person = Person.people.get(name)

        if not person:
            person = Person(name, person_data["age"])

        if person_data.get("wife") is not None:
            person.wife = Person.people.get(person_data["wife"])

        elif person_data.get("husband") is not None:
            person.husband = Person.people.get(person_data["husband"])

        person_list.append(person)

    return person_list
