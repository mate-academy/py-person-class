class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = [Person(person["name"], person["age"]) for person in people]

    for name in people:
        current_name = Person.people[name["name"]]
        husband = name.get("husband")
        wife = name.get("wife")

        if husband:
            current_name.husband = Person.people[husband]
        if wife:
            current_name.wife = Person.people[wife]

    return persons
