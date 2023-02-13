class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self
    pass


def create_person_list(people: list) -> list:

    new_list = [Person(human["name"], human["age"]) for human in people]

    for person in people:
        person_name = Person.people[person["name"]]
        if person.get("wife"):
            person_name.wife =\
                Person.people[person["wife"]]
        if person.get("husband"):
            person_name.husband =\
                Person.people[person["husband"]]
    return new_list
