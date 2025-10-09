class Person:
    people = {}
    
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


from typing import List


def create_person_list(people: List[dict]) -> List[Person]:
    people_list = [
        Person(name=person["name"], age=person["age"])
        for person in people
    ]

    for index, person in enumerate(people):
        if "wife" in person and person["wife"] is not None:
            people_list[index].wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"] is not None:
            people_list[index].husband = Person.people[person["husband"]]

    return people_list
