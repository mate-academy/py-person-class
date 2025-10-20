class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = [Person(person["name"], person["age"]) for person in people]
    for index in range(len(people)):
        if people[index].get("wife", None):
            spouse_name = people[index].get("wife")
            persons[index].wife = Person.people[spouse_name]
        elif people[index].get("husband", None):
            spouse_name = people[index].get("husband")
            persons[index].husband = Person.people[spouse_name]
    return persons
