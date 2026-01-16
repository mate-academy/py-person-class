class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people: list) -> list:
    persons_list = [Person(person["name"], person["age"]) for person in people]
    for pers in range(len(people)):
        if "wife" in people[pers] and people[pers]["wife"] is not None:
            spouse_name = people[pers].get("wife")
            persons_list[pers].wife = Person.people[
                spouse_name
            ]
        if "husband" in people[pers] and people[pers]["husband"] is not None:
            spouse_name = people[pers].get("husband")
            persons_list[pers].husband = Person.people[
                spouse_name
            ]
    return persons_list
