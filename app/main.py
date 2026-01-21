class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(persons_data: list) -> list:
    Person.people.clear()

    person_list = [
        Person(data["name"], data["age"])
        for data in persons_data
    ]

    for data in persons_data:
        current_person = Person.people[data["name"]]

        spouse_name = data.get("husband")
        if spouse_name:
            current_person.husband = Person.people[spouse_name]

        spouse_name = data.get("wife")
        if spouse_name:
            current_person.wife = Person.people[spouse_name]

    return person_list
