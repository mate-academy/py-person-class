class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = []
    for persons in people:
        result_list.append(Person(persons.get("name"), persons.get("age")))
    for new_persons in Person.people:
        for add_person in people:
            if new_persons == add_person.get("name"):
                if "wife" in add_person and add_person.get("wife") is not None:
                    Person.people[new_persons].wife = Person.people[
                        add_person.get("wife")
                    ]
                if (
                    "husband" in add_person
                    and add_person.get("husband") is not None
                ):
                    Person.people[new_persons].husband = Person.people[
                        add_person.get("husband")
                    ]
    return result_list
