class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.age = age
        self.name = name

        Person.people[self.name] = self

    def couple_connection(self, couple_name: str, couple_attr: str) -> None:
        if couple_name in Person.people:
            setattr(self, couple_attr, Person.people[couple_name])


def create_person_list(people: list) -> list:
    people_list = []
    for human in people:
        person_instance = Person(human["name"], human["age"])
        people_list.append(person_instance)

    for human in people:
        person = Person.people[human["name"]]
        if "wife" in human and human["wife"]:
            person.couple_connection(human["wife"], "wife")

        if "husband" in human and human["husband"]:
            person.couple_connection(human["husband"], "husband")

    return people_list
