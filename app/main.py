class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for index, person_data in enumerate(people):
        wife_name = person_data.get("wife")
        if wife_name is not None:
            person_list[index].wife = Person.people[wife_name]
        husband_name = person_data.get("husband")
        if husband_name is not None:
            person_list[index].husband = Person.people[husband_name]
    return person_list
