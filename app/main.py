class Person:
    people = {}

    def __init__(self, name: str, age: int, **kwargs) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self

    def __str__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"


def create_person_list(people: list) -> list:
    objects_people = [
        Person(
            name=person["name"],
            age=person["age"]
        )
        for person in people
    ]
    for person, object_person in zip(people, objects_people):
        if "wife" in person and person.get("wife") is not None:
            object_person.wife = Person.people.get(person["wife"])
        elif "husband" in person and person.get("husband") is not None:
            object_person.husband = Person.people.get(person["husband"])
    return objects_people


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]
