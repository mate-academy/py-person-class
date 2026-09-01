class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(item["name"], item["age"]) for item in people]

    for item, person in zip(people, person_list):
        spouse_key = "wife" if "wife" in item else "husband"
        spouse_name = item[spouse_key]
        if spouse_name is not None:
            setattr(person, spouse_key, Person.people[spouse_name])

    return person_list
