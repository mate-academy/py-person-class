class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self
        self.wife = None
        self.husband = None


def create_person_list(people: list) -> list:
    person_list = []

    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
        person_list.append(person)

    for person in person_list:
        person_data = None
        for data in people:
            if data["name"] == person.name:
                person_data = data
                break

        if person_data is not None:
            if "wife" in person_data and person_data["wife"] is not None:
                if person_data["wife"] in Person.people:
                    person.wife = Person.people[person_data["wife"]]
            else:
                del person.wife

        if "husband" in person_data and person_data["husband"] is not None:
            if person_data["husband"] in Person.people:
                person.husband = Person.people[person_data["husband"]]
        else:
            del person.husband

    return person_list
