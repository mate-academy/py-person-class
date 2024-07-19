class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = [Person(people[i]["name"], people[i]["age"])
               for i in range(len(people))]

    names = {p.name: p for p in persons}

    for i, someone in enumerate(people):
        if someone.get("wife") is not None:
            persons[i].wife = names[someone["wife"]]
        if someone.get("husband") is not None:
            persons[i].husband = names[someone["husband"]]
    return persons
