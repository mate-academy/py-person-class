class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
        person_list.append(person)

    for spouse in people:
        person = Person.people[spouse["name"]]
        if "wife" in spouse and spouse["wife"]:
            person.wife = Person.people[spouse["wife"]]
        elif "husband" in spouse and spouse["husband"]:
            person.husband = Person.people[spouse["husband"]]

    return person_list
