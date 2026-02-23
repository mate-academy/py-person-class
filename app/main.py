class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    return_list = []
    Person.people = {}
    for person in people:
        return_list.append(Person(person["name"], person["age"]))
    for i, person in enumerate(people):
        if person.get("wife", None) is not None:
            return_list[i].wife = Person.people[person["wife"]]
        elif person.get("husband", None) is not None:
            return_list[i].husband = Person.people[person["husband"]]
    return return_list
