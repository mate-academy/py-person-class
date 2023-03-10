class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        current_person = Person(person["name"], person["age"])

        if "wife" in person and person["wife"] in Person.people:
            create_marriage_by_wife(current_person, person["wife"])

        if "husband" in person and person["husband"] in Person.people:
            create_marriage_by_husband(current_person, person["husband"])

        person_list.append(current_person)
    return person_list


def create_marriage_by_husband(
        current_person: Person, husband_name: str
) -> None:
    Person.people[husband_name].wife = current_person
    current_person.husband = Person.people[husband_name]


def create_marriage_by_wife(
        current_person: Person, wife_name: str
) -> None:
    Person.people[wife_name].husband = current_person
    current_person.wife = Person.people[wife_name]
