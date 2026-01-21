class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self
    pass


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = []

    for person_dict in people:
        person_list.append(
            Person(
                person_dict["name"],
                person_dict["age"],
            )
        )

    for person_dict in people:
        name = person_dict["name"]
        person = Person.people[name]
        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            person.wife = Person.people[wife_name]
        elif "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            person.husband = Person.people[husband_name]

    return person_list
