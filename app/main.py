class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    persons = []

    for one_person in people:
        persons.append(Person(one_person["name"], one_person["age"]))

    def find_partner(partner: str, person_list: list) -> Person:
        for someone in person_list:
            if someone.name == partner:
                return someone

    for person in persons:
        for one_person in people:
            if person.name == \
                    one_person.get("name") and one_person.get("wife"):
                person.wife = \
                    find_partner(one_person.get("wife"), persons)
            if person.name == \
                    one_person.get("name") and one_person.get("husband"):
                person.husband = \
                    find_partner(one_person.get("husband"), persons)

    return persons
