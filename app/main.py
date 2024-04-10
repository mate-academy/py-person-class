class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({name: self})


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        new_person = Person(person["name"], person["age"])
        person_list.append(new_person)

    for i, person in enumerate(people):
        spouse = person.get("wife") or person.get("husband")
        if spouse is not None:
            setattr(
                person_list[i],
                "wife" if "wife" in person else "husband",
                Person.people.get(spouse)
            )

    return person_list
