class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    for person_data in people_data:
        name = person_data["name"]
        age = person_data["age"]
        Person(name, age)

    for person_data in people_data:
        name = person_data["name"]
        person_instance = Person.people[name]

        if wife_name := person_data.get("wife"):
            person_instance.wife = Person.people[wife_name]

        if husband_name := person_data.get("husband"):
            person_instance.husband = Person.people[husband_name]

    return [Person.people[person_data["name"]] for person_data in people_data]
