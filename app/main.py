class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_person = [Person(person["name"], person["age"]) for person in people]
    for i in range(len(people)):
        if people[i].get("wife", None):
            spouse_name = people[i].get("wife")
            list_person[i].wife = Person.people[spouse_name]
        elif people[i].get("husband", None):
            spouse_name = people[i].get("husband")
            list_person[i].husband = Person.people[spouse_name]
    return list_person
