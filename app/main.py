class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    person_list = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for person_data, person_instance in zip(people, person_list):
        wife_name = person_data.get("wife")
        husband_name = person_data.get("husband")

        if wife_name is not None:
            person_instance.wife = Person.people[wife_name]

        if husband_name is not None:
            person_instance.husband = Person.people[husband_name]

    return person_list
