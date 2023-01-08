class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.age = age
        self.name = name
        Person.people[f"{self.name}"] = self


def create_person_list(people: list) -> list:
    result_list = []
    for person in people:
        result_list.append(Person(name=person["name"], age=person["age"]))
    for person in people:
        if "wife" in person.keys():
            if person["wife"] is not None:
                person_wife = Person.people[person["wife"]]
                Person.people[person["name"]].wife = person_wife
        if "husband" in person.keys():
            if person["husband"] is not None:
                person_husband = Person.people[person["husband"]]
                Person.people[person["name"]].husband = person_husband
    return result_list
