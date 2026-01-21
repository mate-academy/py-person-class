class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self

    def __repr__(self) -> str:
        return """Person(name="{0}", age={1})""".format(self.name, self.age)


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()

    result: list[Person] = []
    for data in people:
        result.append(Person(data["name"], data["age"]))

    for data in people:
        person = Person.people[data["name"]]
        for key in ("wife", "husband"):
            spouse_name = data.get(key)
            if spouse_name is not None:
                if spouse_name not in Person.people:
                    error_message = (
                        """Spouse "{0}" for "{1}" """
                        """not found in people list"""
                    ).format(spouse_name, person.name)
                    raise ValueError(error_message)
                setattr(person, key, Person.people[spouse_name])

    return result
