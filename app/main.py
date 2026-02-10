class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result_list = [Person(p["name"], p["age"]) for p in people]

    for data, person in zip(people, result_list):
        wife_name = data.get("wife")
        if wife_name is not None:
            person.wife = Person.people.get(wife_name)

        husband_name = data.get("husband")
        if husband_name is not None:
            person.husband = Person.people.get(husband_name)

    return result_list
