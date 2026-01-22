class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for index, person in enumerate(people):
        spouse = person.get("wife") or person.get("husband")
        if spouse:
            setattr(
                person_list[index],
                "wife" if "wife" in person else "husband",
                Person.people.get(spouse)
            )

    return person_list
