class Person:
    people = {}
    
    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:

    person_list = []
    for line in people:
        person_list.append(Person(line["name"], line["age"]))

    for obj in people:
        if obj.get("wife") is not None:
            Person.people[obj["name"]].wife = Person.people[obj["wife"]]
        if obj.get("husband") is not None:
            Person.people[obj["name"]].husband = Person.people[obj["husband"]]
    return person_list
