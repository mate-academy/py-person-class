class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people_list: list) -> list:
    new_person_list = []

    for person in people_list:
        new_person = Person(person["name"], person["age"])
        new_person_list.append(new_person)

    for index, person in enumerate(people_list):
        related_persons = Person.people

        if "wife" in person and person["wife"] is not None:
            new_person_list[index].wife = related_persons[person["wife"]]

        if "husband" in person and person["husband"] is not None:
            new_person_list[index].husband = related_persons[person["husband"]]

    return new_person_list
