class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person_data["name"],
                          person_data["age"])
                   for person_data in people]

    for ind, person_data in enumerate(people):
        if "wife" in person_data and person_data["wife"] is not None:
            person_list[ind].wife = Person.people[people[ind]["wife"]]
        elif "husband" in person_data and person_data["husband"] is not None:
            person_list[ind].husband = Person.people[people[ind]["husband"]]

    return person_list
