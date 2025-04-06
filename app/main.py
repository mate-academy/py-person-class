class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        spouse = Person.people[person["name"]]

        if person.get("wife") is not None:
            spouse.wife = Person.people[person["wife"]]

        elif person.get("husband") is not None:
            spouse.husband = Person.people[person["husband"]]
    return person_list


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]
