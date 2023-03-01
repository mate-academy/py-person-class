class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_persons = [
        Person(persona["name"], persona["age"]) for persona in people
    ]
    for human in people:
        if human.get("wife") is not None:
            Person.people[human["name"]].wife = Person.people[human["wife"]]
        if human.get("husband") is not None:
            Person.people[human["name"]].husband = Person.people[human["husband"]]
    return list_of_persons
