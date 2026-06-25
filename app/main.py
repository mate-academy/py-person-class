class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    my_list = []
    for elem in people:
        Person(elem["name"], elem["age"])
    for elem in people:
        if elem.get("wife") is not None:
            Person.people[elem["name"]].wife = Person.people[elem["wife"]]
        elif elem.get("husband") is not None:
            Person.people[elem["name"]].husband\
                = Person.people[elem["husband"]]
        my_list.append(Person.people[elem["name"]])
    return my_list
