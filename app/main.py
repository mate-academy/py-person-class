class Person:
    people = {}  # class attribute to store all instances by name

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_dicts: list) -> list:
    """Створює список Person інстансів із словників."""
    persons = [Person(p["name"], p["age"]) for p in people_dicts]

    for person in people_dicts:
        person_object = Person.people[person["name"]]
        if person.get("wife") is not None:
            person_object.wife = Person.people[person["wife"]]
        if person.get("husband") is not None:
            person_object.husband = Person.people[person["husband"]]

    return persons


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"},
]
