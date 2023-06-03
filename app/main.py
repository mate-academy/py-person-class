class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    list_of_persons = [Person(name=person["name"], age=person["age"])
                       for person in people]
    for person in people:
        if "husband" in person and person["husband"] is not None:
            Person.people.get(person["name"]).husband = \
                Person.people.get(person["husband"])
        elif "wife" in person and person["wife"] is not None:
            Person.people.get(person["name"]).wife = \
                Person.people.get(person["wife"])
    return list_of_persons
