class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    instances_list = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for index, person_info in enumerate(people):
        husband = person_info.get("husband")
        wife = person_info.get("wife")

        if wife:
            instances_list[index].wife = Person.people.get(wife)

        if husband is not None:
            instances_list[index].husband = Person.people.get(husband)

    return instances_list
