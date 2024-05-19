class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = []
    for person in people:
        result_list.append(Person(person["name"], person["age"]))

    for person in people:
        if person.get("wife") is not None:
            instance = Person.people[person["name"]]
            instance.wife = Person.people[person["wife"]]
        elif person.get("husband") is not None:
            instance = Person.people[person["name"]]
            instance.husband = Person.people[person["husband"]]
    return list(Person.people.values())
