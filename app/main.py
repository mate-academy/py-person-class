class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    result = [Person(person["name"], person["age"])for person in people]
    for person_info in people:
        current_person = (
            Person.people)[person_info["name"]]
        if person_info.get("wife") is not None:
            current_person.wife = Person.people[person_info["wife"]]
        if person_info.get("husband") is not None:
            current_person.husband = Person.people[person_info["husband"]]
    return result
