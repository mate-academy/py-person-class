class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = [Person(per["name"], per["age"]) for per in people]
    for per, value in zip(persons, people):
        if "wife" in value and value["wife"]:
            for count in Person.people:
                if count == value["wife"]:
                    per.wife = Person.people[count]
        if "husband" in value and value["husband"]:
            for count in Person.people:
                if count == value["husband"]:
                    per.husband = Person.people[count]
    return persons
