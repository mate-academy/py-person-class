class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    instances = []

    for person in people:
        name = person["name"]
        age = person["age"]

        person_instance = Person(name, age)
        instances.append(person_instance)

    for person in people:
        name = person["name"]

        if "wife" in person or "husband" in person:
            spouse_key = "wife" if "wife" in person else "husband"
            spouse_name = person[spouse_key]

            if spouse_name is not None:
                if spouse_name in Person.people:
                    person_instance = Person.people[name]
                    spouse_instance = Person.people[spouse_name]

                    setattr(person_instance, spouse_key, spouse_instance)
                else:
                    print(
                        f'Warning: Spouse "{spouse_name}" for "{name}" '
                        f'not found.'
                    )

    return instances
