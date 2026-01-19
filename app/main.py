class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(person["name"], person["age"]) for person in people]

    for i in range(len(people)):
        person_data = people[i]
        person_object = result[i]
        wife_name = person_data.get("wife")
        husband_name = person_data.get("husband")
        if wife_name is not None:
            person_object.wife = Person.people[wife_name]
        if husband_name is not None:
            person_object.husband = Person.people[husband_name]

    return result
