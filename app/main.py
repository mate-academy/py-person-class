class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    Person.people = {}

    for person_data in people_data:
        Person(person_data["name"], person_data["age"])

    for person_data in people_data:
        person = Person.people[person_data["name"]]
        if "wife" in person_data and person_data["wife"]:
            person.wife = Person.people[person_data["wife"]]
            person.wife.husband = person  # Linking back to the husband
        elif "husband" in person_data and person_data["husband"]:
            person.husband = Person.people[person_data["husband"]]
            person.husband.wife = person  # Linking back to the wife

    return [Person.people[person_data["name"]] for person_data in people_data]
