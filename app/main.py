class Person:
    people = {}

    def __init__(self, name, age):
        # type: (str, int) -> None
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people):
    # type: (list[dict]) -> list
    Person.people = {}

    result = [Person(person_data["name"], person_data["age"]) for person_data in people]

    for person_data in people:
        person = Person.people[person_data["name"]]

        wife = person_data.get("wife")
        if wife is not None:
            setattr(person, "wife", Person.people[wife])

        husband = person_data.get("husband")
        if husband is not None:
            setattr(person, "husband", Person.people[husband])

    return result


