class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    for new_person in people:
        new_person = Person(new_person["name"], new_person["age"])

    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        elif person.get("husband"):
            Person.people[person["name"]].husband =\
                Person.people[person["husband"]]
    return [person for person in Person.people.values()]
