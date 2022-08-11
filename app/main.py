class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    people_new = []
    for man in people:
        people_new.append((Person(man['name'], man['age'])))
    for i, man in enumerate(people):
        if "wife" in man and man["wife"] is not None:
            people_new[i].wife = Person.people[man["wife"]]
        if "husband" in man and man["husband"] is not None:
            people_new[i].husband = Person.people[man['husband']]
    return people_new
