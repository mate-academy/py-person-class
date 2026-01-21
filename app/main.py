class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    new_person_list = []
    for person_data in people:
        new_person = Person(person_data["name"], person_data["age"])
        new_person_list.append(new_person)
    for person_data in people:
        person = Person.people[person_data["name"]]
        if person_data.get("wife") is not None:
            person.wife = Person.people[person_data["wife"]]
        if person_data.get("husband") is not None:
            person.husband = Person.people[person_data["husband"]]
    return new_person_list
