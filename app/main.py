class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_list: list) -> list:
    Person.people.clear()
    out_list = []
    for human in people_list:
        new_person = Person(human["name"], human["age"])
        if human.get("husband"):
            new_person.husband = human["husband"]
        elif human.get("wife"):
            new_person.wife = human["wife"]
        out_list.append(new_person)

    for name, human in Person.people.items():
        if hasattr(human, "wife"):
            human.wife = Person.people[human.wife]
        elif hasattr(human, "husband"):
            human.husband = Person.people[human.husband]

    return out_list
