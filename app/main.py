class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person_data in people:
        person_name = person_data["name"]
        if person_name not in Person.people:
            Person(person_data["name"], person_data["age"])

    for person_data in people:
        person = Person.people[person_data["name"]]

        if "wife" in person_data and person_data["wife"] in Person.people:
            person.wife = Person.people[person_data["wife"]]
        elif "wife" in person_data and person_data["wife"] is not None:
            person.wife = None

        if "husband" in person_data\
                and person_data["husband"] in Person.people:
            person.husband = Person.people[person_data["husband"]]

    return list(Person.people.values())
