class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_people = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for index, person in enumerate(people):
        if wife_name := person.get("wife"):
            list_of_people[index].wife = Person.people[wife_name]
        elif husband_name := person.get("husband"):
            list_of_people[index].husband = Person.people[husband_name]

    return list_of_people
