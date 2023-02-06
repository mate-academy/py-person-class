class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = [Person(name=human["name"], age=human["age"])
               for human in people]
    for human in people:
        if "wife" in human and human["wife"]:
            Person.people[human["name"]].wife = Person.people[human["wife"]]
        elif "husband" in human and human["husband"]:
            Person.people[human["name"]].husband\
                = Person.people[human["husband"]]
    return persons
