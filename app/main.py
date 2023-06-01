class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(person["name"], person["age"]) for person in people]

    for index, person in enumerate(people):
        if person.get("wife") is not None:
            people_list[index].wife = Person.people[person["wife"]]
        elif person.get("husband") is not None:
            people_list[index].husband = Person.people[person["husband"]]

    return people_list
