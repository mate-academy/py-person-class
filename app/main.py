class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [
        Person(a_person["name"], a_person["age"])
        for a_person in people
    ]

    for a_person in people:
        result_person = Person.people[a_person["name"]]

        wife_name = a_person.get("wife")
        if wife_name and wife_name in Person.people:
            result_person.wife = Person.people[a_person["wife"]]

        husband_name = a_person.get("husband")
        if husband_name and husband_name in Person.people:
            result_person.husband = Person.people[a_person["husband"]]

    return result
