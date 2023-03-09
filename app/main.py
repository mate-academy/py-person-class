class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    list_of_per = [Person(body["name"], body["age"]) for body in people]
    for human in people:
        if human.get("wife") is not None:
            Person.people[human["name"]].wife = Person.people[human["wife"]]
        elif human.get("husband") is not None:
            Person.people[human["name"]].husband \
                = Person.people[human["husband"]]

    return list_of_per
