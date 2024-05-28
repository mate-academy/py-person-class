class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_person = [Person(person["name"], person["age"]) for person in people]
    for i in range(len(people)):
        if people[i].get("husband", 0):
            list_person[i].husband = Person.people[people[i].get("husband")]
        if people[i].get("wife", 0):
            list_person[i].wife = Person.people[people[i].get("wife")]
    return list_person
