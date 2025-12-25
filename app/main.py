class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(human["name"], human["age"]) for human in people]
    for person in people:
        if person.get("wife") is not None:
            for man in people_list:
                if man.name == person["name"]:
                    man.wife = Person.people[person["wife"]]
        if person.get("husband") is not None:
            for woman in people_list:
                if woman.name == person["name"]:
                    woman.husband = Person.people[person["husband"]]
    return people_list
