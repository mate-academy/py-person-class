class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = []
    for person in people:
        persons.append(Person(person["name"], person["age"]))

    # add attribute wife/husband
    for man in people:
        if "wife" in man:
            for key in Person.people.keys():
                if man["wife"] == key:
                    Person.people[man["name"]].wife = Person.people[key]
                    break

        if "husband" in man:
            for key in Person.people.keys():
                if man["husband"] == key:
                    Person.people[man["name"]].husband = Person.people[key]
                    break

    return persons
