class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for persona in people:
        person = Person.people.get(persona["name"])
        wife_name = persona.get("wife")
        husband_name = persona.get("husband")
        if wife_name and wife_name in Person.people:
            person.wife = Person.people[wife_name]
        if husband_name and husband_name in Person.people:
            person.husband = Person.people[husband_name]
    return person_list
