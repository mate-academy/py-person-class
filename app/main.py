class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person = [Person(persona.get("name"), persona.get("age"))
              for persona in people]
    for person_in_dict in people:
        for key, value in person_in_dict.items():
            if key == "wife" and value is not None:
                Person.people[person_in_dict.get("name")].wife \
                    = Person.people[value]
            if key == "husband" and value is not None:
                Person.people[person_in_dict.get("name")].husband \
                    = Person.people[value]
    return person
