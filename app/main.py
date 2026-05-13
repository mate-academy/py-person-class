class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    list_objs = []
    for person in people:
        person_obj = Person(person.get("name"), person.get("age"))
        list_objs.append(person_obj)
    for i in range(len(list_objs)):
        if people[i].get("wife"):
            list_objs[i].wife = Person.people[people[i]["wife"]]
        elif people[i].get("husband"):
            list_objs[i].husband = Person.people[people[i]["husband"]]
    return list_objs
