class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    spouse = ("wife", "husband")
    persons = []

    for person in people:
        new_person = Person(person["name"], person["age"])
        persons.append(new_person)

    for person in people:
        for partner in spouse:
            if person.get(partner):
                setattr(
                    Person.people[person["name"]],
                    partner,
                    Person.people[person[partner]],
                )

    return persons
