class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for i in people:
        Person(i["name"], i["age"])

    for i in people:
        name = i["name"]
        human = Person.people[name]

        if "wife" in i and i["wife"]:
            human.wife = Person.people[i["wife"]]
            if hasattr(human, "husband"):
                del human.husband

        elif "husband" in i and i["husband"]:
            human.husband = Person.people[i["husband"]]
            if hasattr(human, "wife"):
                del human.wife

        else:
            if hasattr(human, "wife"):
                del human.wife
            if hasattr(human, "husband"):
                del human.husband

    return list(Person.people.values())
