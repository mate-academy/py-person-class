class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_data: list) -> list:
    for person in people_data:
        Person(person.get("name"), person.get("age"))
    for person in people_data:
        name = person.get("name")
        wife_name = person.get("wife")
        husband_name = person.get("husband")
        if name and wife_name is not None:
            setattr(
                Person.people.get(name),
                "wife",
                Person.people.get(wife_name)
            )
        if name and husband_name is not None:
            setattr(
                Person.people.get(name),
                "husband",
                Person.people.get(husband_name),
            )
    result = [Person.people.get(p.get("name")) for p in people_data]

    return result
