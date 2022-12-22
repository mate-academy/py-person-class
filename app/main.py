class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(data: list) -> list:
    persons_instances = [Person(element["name"], element["age"])
                         for element in data]
    for human in data:
        if "wife" in human and human["wife"] is not None:
            Person.people[human["name"]].wife =\
                Person.people[human["wife"]]
        elif "husband" in human and human["husband"] is not None:
            Person.people[human["name"]].husband =\
                Person.people[human["husband"]]

    return persons_instances
