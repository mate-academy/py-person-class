class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for personal_data in people:
        Person(personal_data["name"], personal_data["age"])

    for personal_data in people:
        name = personal_data["name"]
        person = Person.people[name]
        if "wife" in personal_data and personal_data["wife"]:
            person.wife = Person.people[personal_data["wife"]]
        elif "husband" in personal_data and personal_data["husband"]:
            person.husband = Person.people[personal_data["husband"]]

    return list(Person.people.values())
