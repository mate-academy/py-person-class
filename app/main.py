class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_data in people:
        person_name = person_data["name"]
        if person_name in Person.people:
            person = Person.people[person_name]
        else:
            person = Person(person_name, person_data["age"])
        if "wife" in person_data and person_data["wife"] in Person.people:
            person.wife = Person.people[person_data["wife"]]
        elif "wife" in person_data and person_data["wife"] is not None:
            person.wife = None
        if "husband" in person_data \
                and person_data["husband"] in Person.people:
            person.husband = Person.people[person_data["husband"]]
        person_list.append(person)
    return person_list
