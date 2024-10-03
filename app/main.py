class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    person_instances = []

    person_instances = [Person(person["name"],
                               person["age"]) for person in people_list]

    people_dict = {p["name"]: p for p in people_list}

    for person in person_instances:
        if original_person := people_dict.get(person.name):
            spouse_key = "wife" if "wife" in original_person else "husband"
            if spouse_name := original_person.get(spouse_key):
                setattr(person, spouse_key, Person.people[spouse_name])

    return person_instances
