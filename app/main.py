class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def __setattr__(self, key: str, value: str) -> None:
        if key in {"wife", "husband"}:
            if value is not None:
                object.__setattr__(self, key, value)
        else:
            super().__setattr__(key, value)


def create_person_list(people: list) -> list:
    for person in people:
        name = person["name"]
        age = person["age"]
        Person(name, age)

    for person in people:
        name = person["name"]
        instance = Person.people[name]
        wife_name = person.get("wife")
        husband_name = person.get("husband")

        if wife_name:
            instance.wife = Person.people.get(wife_name)
        if husband_name:
            instance.husband = Person.people.get(husband_name)

    return list(Person.people.values())
