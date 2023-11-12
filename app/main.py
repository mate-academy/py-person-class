class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        new_person = Person(
            person["name"],
            person["age"]
        )
        person_list.append(new_person)
    persons = person_list[0].people
    for person in people:
        if "wife" in person.keys() and person["wife"] is not None:
            persons[person["name"]].wife = persons[person["wife"]]
        if "husband" in person.keys() and person["husband"] is not None:
            persons[person["name"]].husband = persons[person["husband"]]
    return person_list
