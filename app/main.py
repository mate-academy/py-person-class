class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    persons = [Person(entry.get("name"), entry.get("age")) for entry in people]

    for entry in people:
        person = Person.people.get(entry.get("name"))
        if not person:
            continue

        for spouse in ["wife", "husband"]:
            if (
                (name := entry.get(spouse))
                and (spouse_obj := Person.people.get(name))
            ):
                setattr(person, spouse, spouse_obj)

    return persons
