class Person:
    people = {}   # class attribute

    def __init__(self, name: str, age: int) -> None:
        self.name = name  # instance attribute
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    person_list = []

    for element in people:
        person = Person(element["name"], element["age"])
        person_list.append(person)

    for element in people:
        now_person = Person.people[element["name"]]
        if "wife" in element and element["wife"] is not None:
            now_person.wife = Person.people[element["wife"]]

        if "husband" in element and element["husband"] is not None:
            now_person.husband = Person.people[element["husband"]]

    return person_list
