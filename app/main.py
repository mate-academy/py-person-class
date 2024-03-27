class Person:
    people = {}

    def __init__(self, name:str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for human in people:
        result.append(Person(human["name"],human["age"]))
    for human in people:
        if human.get("wife"):
            result[people.index(human)].wife = Person.people[human["wife"]]
        elif human.get("husband"):
            result[people.index(human)].husband = (
                Person.people)[human["husband"]]
    return result
