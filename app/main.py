class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    persons = []
    for item in people:
        person = Person(item["name"], item["age"])
        persons.append(person)

    for item in people:
        person = Person.people[item["name"]]

        if "wife" in item and item["wife"]:
            person.wife = Person.people[item["wife"]]

        if "husband" in item and item["husband"]:
            person.husband = Person.people[item["husband"]]

    return persons
