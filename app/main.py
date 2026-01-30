class Person:
    people = {}

    def __init__(self, name: str, age: int, **kwargs) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    person_class_list = [Person(**person) for person in people]

    for person in people:
        spouse_key = "husband" if person.get("husband") else "wife" \
            if person.get("wife") else None

        if spouse_key:
            person_instance = Person.people[person["name"]]
            person_spouse = Person.people[person[spouse_key]]

            setattr(person_instance, spouse_key, person_spouse)
    return person_class_list
