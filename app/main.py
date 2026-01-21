class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    res_list = []

    for dic in people:
        res_list.append(Person(dic["name"], dic["age"]))
    for dic in people:
        if None in dic.values():
            continue
        elif "wife" in dic.keys():
            Person.people[dic["name"]].wife = Person.people[dic["wife"]]
        elif "husband" in dic.keys():
            Person.people[dic["name"]].husband = Person.people[dic["husband"]]

    return res_list
