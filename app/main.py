class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = []

    for person_info in people:
        name = person_info["name"]
        age = person_info["age"]
        person = Person(name, age)
        persons.append(person)

    for person_info in people:
        name = person_info["name"]
        current_person = Person.people[name]

        if person_info.get("wife"):
            wife_name = person_info["wife"]
            current_person.wife = Person.people[wife_name]

        if person_info.get("husband"):
            husband_name = person_info["husband"]
            current_person.husband = Person.people[husband_name]

    return persons
