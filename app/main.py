class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        person_list.append(new_person)
    for person in people:
        partner_name = person.get("wife") or person.get("husband")
        if partner_name:
            if person.get("wife"):
                Person.people[person["name"]].wife = (
                    Person.people[partner_name]
                )
            else:
                Person.people[person["name"]].husband = (
                    Person.people[partner_name]
                )
    return person_list
