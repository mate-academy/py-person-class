class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = []
    for citizen in people:
        person = Person(citizen["name"], citizen["age"])
        if "wife" in citizen and citizen["wife"] is not None:
            for human in people:
                if citizen["wife"] == human["name"]:
                    person_wife = Person(human["name"], human["age"])
                    person_wife.husband = person
                    person.wife = person_wife
        persons.append(person)
    return persons
