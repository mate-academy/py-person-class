class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    lst = []
    for i in people:
        i = Person(i["name"], i["age"])
        lst.append(i)

    for i in people:
        person = Person.people[i["name"]]
        if i.get("wife") is not None:
            person.wife = Person.people[i["wife"]]
        if i.get("husband") is not None:
            person.husband = Person.people[i["husband"]]
    return lst
