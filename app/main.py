class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = []
    for individual in people:
        person = Person(individual["name"], individual["age"])
        if "wife" in individual and individual["wife"] is not None:
            for partner in people:
                if individual["wife"] == partner["name"]:
                    person_wife = Person(partner["name"], partner["age"])
                    person_wife.husband = person
                    person.wife = person_wife
        persons.append(person)
    return persons
