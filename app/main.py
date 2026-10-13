class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person_data in people:
        name = person_data["name"]
        person = Person.people[name]

        if person_data.get("wife") is not None:
            person.wife = Person.people[person_data["wife"]]

        if person_data.get("husband") is not None:
            person.husband = Person.people[person_data["husband"]]

    return person_list
