class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    [
        Person(p.get("name"), p.get("age"))
        for p in people_data
        if p.get("name") not in Person.people
    ]

    [
        (
            setattr(
                Person.people.get(p.get("name")),
                "wife",
                Person.people.get(p.get("wife"))
            )
            if p.get("wife") is not None else None,
            setattr(
                Person.people.get(p.get("name")),
                "husband",
                Person.people.get(p.get("husband"))
            )
            if p.get("husband") is not None else None
        )
        for p in people_data
    ]

    return [
        Person.people.get(p.get("name")) 
        for p in people_data
    ]
