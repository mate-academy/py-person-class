class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        instance = Person.people[person["name"]]

        spouse_name = person.get("wife")
        if spouse_name:
            instance.wife = Person.people[spouse_name]

        spouse_name = person.get("husband")
        if spouse_name:
            instance.husband = Person.people[spouse_name]

    return persons
