class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    my_list = []
    for man in people:
        my_list.append(Person(man["name"], man["age"]))
    for man in people:
        if man.get("wife"):
            my_list[people.index(man)].wife = Person.people[man["wife"]]
        elif man.get("husband"):
            my_list[people.index(man)].husband = Person.people[man["husband"]]
    return my_list
