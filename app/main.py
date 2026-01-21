class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_persons = [
        Person(someone["name"], someone["age"])
        for someone in people
    ]

    for someone in people:
        someone_person = Person.people[someone["name"]]
        if someone.get("wife"):
            someone_person.wife = Person.people[someone.get("wife")]
        if someone.get("husband"):
            someone_person.husband = Person.people[someone.get("husband")]

    return list_of_persons
