class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result_list = [
        Person(data["name"], data["age"])
        for data in people
    ]

    for data, person in zip(people, result_list):
        if wife_name := data.get("wife"):
            person.wife = Person.people.get(wife_name)

        if husband_name := data.get("husband"):
            person.husband = Person.people.get(husband_name)

    return result_list
