class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    person_l = [Person(person["name"], person["age"]) for person in people]
    for name, person in Person.people.items():
        for per in people:
            if name == per["name"] and "wife" in per and per["wife"]:
                person.wife = Person.people[per["wife"]]
            if name == per["name"] and "husband" in per and per["husband"]:
                person.husband = Person.people[per["husband"]]
    return person_l
