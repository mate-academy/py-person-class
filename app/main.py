class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    to_return = []
    for describe in people:
        current_person = Person(describe["name"], describe["age"])

        if "wife" in describe and describe["wife"] in Person.people:
            create_marriage_by_wife(current_person, describe["wife"])

        if "husband" in describe and describe["husband"] in Person.people:
            create_marriage_by_husband(current_person, describe["husband"])

        to_return.append(current_person)
    return to_return


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
