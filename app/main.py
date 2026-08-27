class Person:
    people = [
        {"name": "Ross", "age": 30, "wife": "Rachel"},
        {"name": "Joey", "age": 29, "wife": None},
        {"name": "Rachel", "age": 28, "husband": "Ross"}
    ]

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    result = []

    for person in people:
        new_person = Person(person["name"], person["age"])

        if "wife" in person:
            new_person.wife = person["wife"]

        if "husband" in person:
            new_person.husband = person["husband"]

        result.append(new_person)

    return result
