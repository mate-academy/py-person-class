class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list:
    Person.people.clear()

    instances = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]

    for person_data in people:
        current_instance = Person.people[person_data["name"]]

        wife_name = person_data.get("wife")
        if wife_name:
            current_instance.wife = Person.people[wife_name]

        husband_name = person_data.get("husband")
        if husband_name:
            current_instance.husband = Person.people[husband_name]

    return instances
