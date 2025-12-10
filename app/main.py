class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    created_people = [
        Person(
            name=person["name"],
            age=person["age"],
        )
        for person in people
    ]

    if not created_people:
        return []

    for person in people:
        if person.get("wife"):
            person_instance = Person.people[person["name"]]
            wife_instance = Person.people[person["wife"]]
            person_instance.wife = wife_instance

        if person.get("husband"):
            person_instance = Person.people[person["name"]]
            husband_instance = Person.people[person["husband"]]
            person_instance.husband = husband_instance

    return created_people
