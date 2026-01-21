class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife=None
        self.husband=None
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    for chel in people:
        Person(chel["name"], chel["age"])

    for chel in people:
        person = Person.people[chel["name"]]
        wife_name = chel.get("wife")
        husband_name = chel.get("husband")

        if wife_name and wife_name in Person.people:
            person.wife = Person.people[wife_name]
        if husband_name and husband_name in Person.people:
            person.husband = Person.people[husband_name]

    return list(Person.people.values())
