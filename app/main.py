class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = [Person(person["name"], person["age"]) for person in people]

    for person_dict in people:
        name = person_dict["name"]
        spouse_key = "wife" if "wife" in person_dict else "husband"
        spouse_name = person_dict.get(spouse_key)

        if spouse_name is not None:
            # Link the spouse attribute to the corresponding Person instance
            setattr(
                Person.people[name],
                spouse_key,
                Person.people[spouse_name]
            )

    return persons
