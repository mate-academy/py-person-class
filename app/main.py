class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(man["name"], man["age"]) for man in people]

    for man in people:
        if man.get("wife"):
            wife = Person.people[man["wife"]]
            person_list[people.index(man)].wife = wife
        if man.get("husband"):
            husband = Person.people[man["husband"]]
            person_list[people.index(man)].husband = husband

    return person_list
