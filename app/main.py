class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
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

    for ind, person_data in enumerate(people):
        if "wife" in person_data and person_data["wife"] is not None:
            person_list[ind].wife = [person for person in person_list
                                     if person.name == person_data["wife"]][0]
        elif "husband" in person_data and person_data["husband"] is not None:
            person_list[ind].husband = [person for person
                                        in person_list
                                        if person.name
                                        == person_data["husband"]][0]

    return person_list
