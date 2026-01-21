class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        name = person["name"]
        instance = Person.people[name]

        if person.get("wife"):
            instance.wife = instance.people[person["wife"]]
        elif person.get("husband"):
            instance.husband = instance.people[person["husband"]]

    return person_list
