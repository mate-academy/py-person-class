class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_person = [
        Person(person["name"], person["age"]) for person in people
    ]
    for name, person in Person.people.items():
        for info in people:
            if name == info["name"] and info.get("wife"):
                person.wife = Person.people[info["wife"]]
            if name == info["name"] and info.get("husband"):
                person.husband = Person.people[info["husband"]]
    return list_of_person
