class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    persones_list = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for index, person in enumerate(people):
        current_person = persones_list[index]

        if person.get("wife"):
            wife_name = person["wife"]
            current_person.wife = Person.people[wife_name]

        if person.get("husband"):
            husband_name = person["husband"]
            current_person.husband = Person.people[husband_name]

    return persones_list
