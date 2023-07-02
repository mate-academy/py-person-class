class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = []
    for human in people:
        person = Person(human["name"], human["age"])
        if "wife" in human and human["wife"] is not None:
            for human1 in people:
                if human["wife"] == human1["name"]:
                    person_wife = Person(human1["name"], human1["age"])
                    person_wife.husband = person
                    person.wife = person_wife
        persons.append(person)

    return persons
