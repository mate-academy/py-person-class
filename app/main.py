class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: dict) -> list:
    # Create all Person instances
    for person in people:
        Person(person["name"], person["age"])

    # Set spouse attributes
    for person in people:
        instance = Person.people[person["name"]]
        wife = person.get("wife")
        husband = person.get("husband")
        if wife:
            instance.wife = Person.people.get(wife)
        if husband:
            instance.husband = Person.people.get(husband)

    return list(Person.people.values())
