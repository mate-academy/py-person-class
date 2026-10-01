class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []

    for person in people:
        result.append(Person(person["name"], person["age"]))

    for person in people:
        me = Person.people[person["name"]]
        if person.get("wife") is not None:
            me.wife = Person.people[person["wife"]]
        elif person.get("husband") is not None:
            me.husband = Person.people[person["husband"]]

    return result
