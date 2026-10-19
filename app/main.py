class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        result.append(new_person)
    for person in people:
        if person.get("husband") is not None:
            current_person = Person.people[person["name"]]
            current_person.husband = Person.people[person["husband"]]
        if person.get("wife") is not None:
            current_person1 = Person.people[person["name"]]
            current_person1.wife = Person.people[person["wife"]]

    return result
