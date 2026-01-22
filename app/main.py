class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])

    person_list = [
        Person.people.get(person.get("name")) for person in people
    ]

    for person in people:
        person_instance = Person.people.get(person.get("name"))
        if "wife" in person and person.get("wife") is not None:
            person_instance.wife = Person.people.get(person.get("wife"))
        if "husband" in person and person.get("husband") is not None:
            person_instance.husband = Person.people.get(person.get("husband"))

    return person_list


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]
