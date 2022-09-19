class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    list_with_person = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for i, person in enumerate(people):
        if person.get("wife") is not None:
            list_with_person[i].wife = Person.people[person["wife"]]
        elif person.get("husband") is not None:
            list_with_person[i].husband = Person.people[person["husband"]]

    return list_with_person
