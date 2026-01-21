class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    person_list = [Person(person["name"], person["age"]) for person in people]

    for person_info in people:
        person_instance = Person.people[person_info["name"]]

        if wife := person_info.get("wife"):
            person_instance.wife = Person.people[wife]
        if husband := person_info.get("husband"):
            person_instance.husband = Person.people[husband]

    return person_list
