class Person:
    # write your code here
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])

    # Second pass: set the wife/husband attributes
    for person in people:
        current_person = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            current_person.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"]:
            current_person.husband = Person.people[person["husband"]]

    return list(Person.people.values())
