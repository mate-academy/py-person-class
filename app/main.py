class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_with_instances = []
    for person in people:
        list_with_instances.append(Person(person["name"], person["age"]))
    for person in people:
        if "wife" in person and person.get("wife") is not None:
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        if "husband" in person and person.get("husband") is not None:
            Person.people[person["name"]].husband = \
                Person.people[person["husband"]]
    return list_with_instances
