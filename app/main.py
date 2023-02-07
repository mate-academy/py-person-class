class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = [Person(name=human["name"], age=human["age"])
               for human in people]
    database = Person.people
    for human in people:
        if "wife" in human and human["wife"]:
            database[human["name"]].wife = database[human["wife"]]
        elif "husband" in human and human["husband"]:
            database[human["name"]].husband = database[human["husband"]]
    return persons
