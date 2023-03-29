class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = []
    for person in people:
        persons.append(Person(person["name"], person["age"]))

    # add attribute wife/husband
    for man in people:
        if "wife" in man:
            if man["wife"] in Person.people:
                wife = Person.people[man.get("wife")]
                Person.people[man.get("name")].wife = wife

        if "husband" in man:
            if man["husband"] in Person.people:
                husband = Person.people[man.get("husband")]
                Person.people[man.get("name")].husband = husband

    return persons
