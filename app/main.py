class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    people_objs = []

    for data in people:
        person_inst = Person(data["name"], data["age"])
        people_objs.append(person_inst)

    for data in people:
        if data.get("wife") in Person.people:
            Person.people[data["name"]].wife \
                = Person.people[data["wife"]]

        elif data.get("husband") in Person.people:
            Person.people[data["name"]].husband \
                = Person.people[data["husband"]]

    return people_objs
