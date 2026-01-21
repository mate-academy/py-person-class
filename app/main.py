class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self

    @classmethod
    def get_or_create(cls, key: str, person: dict) -> "Person":
        person_name = person[key]

        if person_name in cls.people:
            return cls.people[person_name]

        created_person = cls(person_name, person["age"])

        cls.people[person_name] = created_person

        return created_person


def create_person_list(people: list) -> list:
    created_person_list = []

    for person in people:
        created_person = Person.get_or_create("name", person)

        if person.get("wife") is not None:
            created_person.wife = Person.get_or_create("wife", person)

        if person.get("husband") is not None:
            created_person.husband = Person.get_or_create("husband", person)

        created_person_list.append(created_person)

    return created_person_list
