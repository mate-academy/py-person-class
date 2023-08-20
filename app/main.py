class Person:
    people = {}

    def __init__(self,
                 name: str,
                 age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = []
    for citizen in people:
        person = Person(citizen["name"], citizen["age"])
        persons.append(person)

    for citizen in people:
        if "wife" in citizen and citizen["wife"] is not None:
            person = Person.people[citizen["name"]]
            spouse = Person.people[citizen["wife"]]
            person.wife = spouse
            spouse.husband = person

    for person in persons:
        if person.wife is None:
            del person.wife

    return persons
