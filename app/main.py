class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_dicts: list) -> list:
    Person.people = {}
    person_list = [Person(data["name"], data["age"]) for data in people_dicts]
    for data in people_dicts:
        person_instance = Person.people[data["name"]]
        if data.get("wife") is not None:
            wife_name = data["wife"]
            person_instance.wife = Person.people[wife_name]
        elif data.get("husband") is not None:
            husband_name = data["husband"]
            person_instance.husband = Person.people[husband_name]

    return person_list
