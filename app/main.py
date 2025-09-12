class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []

    for person_input in people:
        person = Person(person_input["name"], person_input["age"])
        result.append(person)

    for person_input in people:
        if "wife" in person_input and person_input["wife"] is not None:
            wife = Person.people.get(person_input["wife"], None)
            Person.people[person_input["name"]].wife = wife
        elif "husband" in person_input and person_input["husband"] is not None:
            husband = Person.people.get(person_input["husband"], None)
            Person.people[person_input["name"]].husband = husband

    return result
