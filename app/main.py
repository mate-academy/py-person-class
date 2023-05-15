class Person:
    people = {}

    def __init__(self,
                 name: str,
                 age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        person_list.append(new_person)

    for human in people:
        if human.get("wife") is not None and human["wife"] is not None:
            Person.people[human["name"]].wife = Person.people[human["wife"]]
        elif human.get("husband") is not None and human["husband"] is not None:
            Person.people[human["name"]].husband =\
                Person.people[human["husband"]]
    return person_list
