class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    peoples = []
    for i in range(len(people)):
        human = Person(people[i]["name"], people[i]["age"])
        if "wife" in people[i].keys() \
                and people[i]["wife"] is not None:
            human.wife = people[i]["wife"]
        elif "husband" in people[i].keys() \
                and people[i]["husband"] is not None:
            human.husband = people[i]["husband"]
        peoples.append(human)

    for i in peoples:
        if "wife" in i.__dict__.keys():
            if i.wife in Person.people.keys():
                i.wife = Person.people[i.wife]
        if "husband" in i.__dict__.keys():
            if i.husband in Person.people.keys():
                i.husband = Person.people[i.husband]

    return peoples
