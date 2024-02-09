class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = [
        Person(
            person["name"],
            person["age"]
        )
        for person in people
    ]
    for person in people:
        if wife_name := person.get("wife"):
            wife = Person.people[wife_name]
            wife.husband = Person.people[person["name"]]
            wife.husband.wife = wife

    return people_list
