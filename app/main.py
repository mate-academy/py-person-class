class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = []
    for human in people:
        person = Person(human["name"], human["age"])
        if "wife" in human and human["wife"] is not None:
            for human2 in people:
                if human["wife"] == human2["name"]:
                    person_wife = Person(human2["name"], human2["age"])
                    person_wife.husband = person
                    person.wife = person_wife
        persons.append(person)
    return persons
