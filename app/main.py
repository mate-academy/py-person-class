class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for man in people:
        man = Person(man["name"], man["age"])
        person_list.append(man)
    for i in people:
        if i.get("husband") is not None :
            if Person.people.get(i["husband"]):
                Person.people[i["name"]].husband = Person.people[i["husband"]]
        if i.get("wife") is not None:
            if Person.people.get(i["wife"]):
                Person.people[i["name"]].wife = Person.people[i["wife"]]
    return person_list
