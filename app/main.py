class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    result = [Person(p["name"], p["age"]) for p in people]

    for i in range(len(people)):
        data = people[i]
        person_instance = result[i]

        wife_name = data.get("wife")
        if wife_name is not None:
            person_instance.wife = Person.people[wife_name]

        husband_name = data.get("husband")
        if husband_name is not None:
            person_instance.husband = Person.people[husband_name]

    return result
