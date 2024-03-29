class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(human["name"], human["age"]) for human in people]
    for human in people:
        if human.get("wife"):
            people_list[
                people.index(human)].wife = Person.people[human["wife"]]
        elif human.get("husband"):
            people_list[people.index(human)].husband = (
                Person.people)[human["husband"]]
    return people_list
