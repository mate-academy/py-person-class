class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    list_of_persons = [
        Person(persona["name"], persona["age"]) for persona in people
    ]
    for man in people:
        if man.get("wife") is not None:
            Person.people[man["name"]].wife = Person.people[man["wife"]]
        if man.get("husband") is not None:
            Person.people[man["name"]].husband = Person.people[man["husband"]]
    return list_of_persons
