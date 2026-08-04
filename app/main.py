class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person = []
    for persona in people:
        person.append(Person(persona["name"], persona["age"]))
    for person_in_dict in people:
        for key, value in person_in_dict.items():
            if key == "wife" and value is not None:
                Person.people[person_in_dict["name"]].wife \
                    = Person.people[value]
            if key == "husband" and value is not None:
                Person.people[person_in_dict["name"]].husband \
                    = Person.people[value]
    return person
