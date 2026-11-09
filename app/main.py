class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        self.people[self.name] = self


def create_person_list(people: list) -> list:
    result_list = []
    for person in people:
        result_list.append(Person(person["name"], person["age"]))

    for index, person in enumerate(people):
        if person.get("wife") is not None:
            result_list[index].wife = Person.people[person["wife"]]
        if person.get("husband") is not None:
            result_list[index].husband = Person.people[person["husband"]]
    return result_list
