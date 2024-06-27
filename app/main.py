class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.spouse = None
        self.wife = None
        self.husband = None
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    for person_dict in people_list:
        Person(person_dict["name"], person_dict["age"])

    for person_dict in people_list:
        person = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"] is not None:
            spouse = Person.people[person_dict["wife"]]
            person.spouse = spouse
            person.wife = spouse
            spouse.spouse = person
            spouse.husband = person
        elif "husband" in person_dict and person_dict["husband"] is not None:
            spouse = Person.people[person_dict["husband"]]
            person.spouse = spouse
            person.husband = spouse
            spouse.spouse = person
            spouse.wife = person
        else:
            person.wife = None
            person.husband = None

    for person in Person.people.values():
        if person.wife is None:
            del person.wife
        if person.husband is None:
            del person.husband

    return list(Person.people.values())
