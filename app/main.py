class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.spouse = None
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    new_list = []

    for person in people:
        name = person["name"]
        age = person["age"]
        spouse_name = person.get("wife") or person.get("husband")
        spouse = Person.people.get(spouse_name)
        new_person = Person(name, age)
        new_person.spouse = spouse
        new_list.append(new_person)

    return new_list
