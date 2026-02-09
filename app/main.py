class Person:
    people = {}
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self

def create_person_list(people: list) -> list:
    res = []
    for human in people:
        h_1 = Person(human["name"], human["age"])
        res.append(h_1)
    for person in people:
        instance = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            instance.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"]:
            instance.husband = Person.people[person["husband"]]
    return res
