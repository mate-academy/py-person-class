class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    new_list = [Person(element["name"], element["age"]) for element in people]
    for elem in new_list:
        for element in people:
            if elem.name == element["name"]:
                if element.get("wife") is not None:
                    elem.wife = Person.people[element["wife"]]
                if element.get("husband") is not None:
                    elem.husband = Person.people[element["husband"]]

    return new_list
