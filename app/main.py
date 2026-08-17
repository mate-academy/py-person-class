class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    """
    Zamienia listę słowników z danymi osób na listę
    instancji klasy Person.
    """
    list_person = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        new_obj = Person.people[person["name"]]

        if person.get("wife"):
            new_wife = person["wife"]
            new_obj.wife = Person.people[new_wife]

        if person.get("husband"):
            new_husband = person["husband"]
            new_obj.husband = Person.people[new_husband]

    return list_person


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]
