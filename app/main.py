class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for person in people:
        current_person = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            wife_name = person["wife"]
            if wife_name in Person.people:
                current_person.wife = Person.people[wife_name]

        elif "husband" in person and person["husband"]:
            husband_name = person["husband"]
            if husband_name in Person.people:
                current_person.husband = Person.people[husband_name]

    return persons
