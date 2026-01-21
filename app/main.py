class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person.people[person["name"]] = Person(person["name"], person["age"])
    for person in people:
        if "wife" in person and person.get("wife") is not None:
            wife = Person.people[person.get("wife")]
            Person.people[person.get("name")].wife = wife
        elif "husband" in person and person.get("husband") is not None:
            husband = Person.people[person.get("husband")]
            Person.people[person.get("name")].husband = husband

    return [human for human in Person.people.values()]
