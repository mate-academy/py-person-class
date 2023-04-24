class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for human in people:
        new_member = Person(human["name"], human["age"])
        if "wife" in human and human["wife"] is not None:
            new_member.wife = human["wife"]
        elif "husband" in human and human["husband"] is not None:
            new_member.husband = human["husband"]
        people_list.append(new_member)
    for human in people_list:
        if hasattr(human, "wife"):
            human.wife = Person.people[human.wife]
        elif hasattr(human, "husband"):
            human.husband = Person.people[human.husband]

    return people_list
