class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        self.add_person(self)

    @classmethod
    def add_person(cls, person: Person) -> None:
        cls.people[person.name] = person

    @classmethod
    def get_person(cls, name: str) -> Person:
        return cls.people[name]


def create_person_list(people: list) -> list:
    result_list = [
        Person(name=person["name"], age=person["age"])
        for person in people
    ]

    for person in people:
        current = Person.get_person(person["name"])
        for role in ("wife", "husband"):
            partner_name = person.get(role)
            if partner_name is not None:
                setattr(current, role, Person.get_person(partner_name))

    return result_list
