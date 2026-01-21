class Person:
    people = {}

    def __init__(self, name: str, age: str) -> str:
        self.name = name
        self.age = age
        Person.people[self.name] = self
    pass


def create_person_list(people: list) -> list:
    result = []
    for peoples in people:
        result.append(Person(peoples["name"], peoples["age"]))
    for peoples_2 in people:
        if peoples_2.get("wife") is not None:
            Person.people[peoples_2.get("name")].wife \
                = Person.people[peoples_2.get("wife")]
        if peoples_2.get("husband") is not None:
            Person.people[peoples_2.get("name")].husband \
                = Person.people[peoples_2.get("husband")]
    return result
    pass
