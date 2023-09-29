class Person:
    people = {}

    def __init__(self, name: str, age: int, *args) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:

    persons = [Person(per["name"], per["age"]) for per in people_list]

    for people, value in zip(persons, people_list):
        if "wife" in value and value["wife"]:
            for count in Person.people:
                if count == value["wife"]:
                    people.wife = Person.people[count]
        if "husband" in value and value["husband"]:
            for count in Person.people:
                if count == value["husband"]:
                    people.husband = Person.people[count]
    return persons
