class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    w = "wife"
    n = "name"
    h = "husband"
    a = "age"
    for person in people:
        person_list.append(Person(person[n], person[a]))
    for human in people:
        if w in human:
            if human[w] is not None:
                Person.people[human[n]].wife = Person.people[human[w]]
        if h in human:
            if human[h] is not None:
                Person.people[human[n]].husband = Person.people[human[h]]
    return person_list
