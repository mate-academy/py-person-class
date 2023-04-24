class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for human in people:
        person = Person(human["name"], human["age"])
        person_list.append(person)

    for human in people:
        if "wife" in human and human["wife"] is not None:
            Person.people[human["name"]].wife\
                = Person.people[human["wife"]]
        if "husband" in human and human["husband"] is not None:
            Person.people[human["name"]].husband\
                = Person.people[human["husband"]]
    return person_list
