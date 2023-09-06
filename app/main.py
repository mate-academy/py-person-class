class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:

    people_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        person_partner = person.get("wife") or person.get("husband")
        if person_partner:
            person_inst = Person.people[person["name"]]
            married_inst = Person.people[person_partner]

            if "husband" in person:
                person_inst.husband = married_inst
            if "wife" in person:
                person_inst.wife = married_inst

    return people_list
