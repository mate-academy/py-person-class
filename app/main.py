class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self

    @classmethod
    def add_partner(cls, name: str, partner: str, is_husband: bool) -> None:
        person = cls.people[name]
        partner = cls.people[partner]

        if is_husband:
            person.husband = partner
        else:
            person.wife = partner


def create_person_list(people: list) -> list:
    person_list = [
        Person(name=person["name"], age=person["age"])
        for person in people
    ]

    for raw_person in people:
        name = raw_person["name"]

        wife_name = raw_person.get("wife")
        if wife_name:
            Person.add_partner(name, wife_name, False)

        husband_name = raw_person.get("husband")
        if husband_name:
            Person.add_partner(name, husband_name, True)

    return person_list
