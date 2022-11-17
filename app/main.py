class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people.update({name: self})


def create_person_list(people: list) -> list:
    person_list = []
    for pe in people:
        person_list.append(Person(pe["name"], pe["age"]))
    for i, pe in enumerate(people):
        if "wife" in pe and pe["wife"]:
            person_list[i].wife = Person.people[pe["wife"]]
        elif "husband" in pe and pe["husband"]:
            person_list[i].husband = Person.people[pe["husband"]]
    return person_list
