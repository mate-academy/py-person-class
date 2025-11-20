class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    persons = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        name = person["name"]
        obj = Person.people[name]

        wife_name = person.get("wife")
        if wife_name and wife_name in Person.people:
            obj.wife = Person.people[wife_name]

        husband_name = person.get("husband")
        if husband_name and husband_name in Person.people:
            obj.husband = Person.people[husband_name]

    return persons
