class Person:
    people = {}

    def __init__(self, name: str, age: float) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    # Create all Person objects using list comprehension [CHECKLIST #3]
    person_list = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]

    for person_data in people:
        person = Person.people[person_data["name"]]
        for key, value in person_data.items():
            # Combined nested if statements [CHECKLIST #2]
            is_valid_key = key not in ["name", "age"]
            is_person_reference = (isinstance(value, str)
                                   and value in Person.people)

            if is_valid_key and is_person_reference:
                setattr(person, key, Person.people[value])
            elif is_valid_key and value is not None:
                setattr(person, key, value)

    return person_list
