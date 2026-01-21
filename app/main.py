class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        single = Person(name=person["name"], age=person["age"])
        result.append(single)

    for person in people:
        name = person["name"]
        instance = Person.people[name]
        if person.get("wife"):
            instance.wife = Person.people[person["wife"]]
        elif person.get("husband"):
            instance.husband = Person.people[person["husband"]]

    return result
