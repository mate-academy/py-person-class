class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"],
                          person.get("age"))
                   for person in people]

    relationship = [(person["name"],
                     person.get("wife"), person.get("husband"))
                    for person in people]

    for name, wife_name, husband_name in relationship:
        person = Person.people[name]

        if wife_name:
            person.wife = Person.people.get(wife_name)

        if husband_name:
            person.husband = Person.people.get(husband_name)

    return person_list
