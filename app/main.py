class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(person_data_list: list) -> list:
    person_objects = []

    for person_data in person_data_list:
        person_obj = Person(person_data["name"], person_data["age"])
        person_objects.append(person_obj)

    for person_data in person_data_list:
        person_name = person_data["name"]
        if person_data.get("wife"):
            spouse_name = person_data["wife"]
            Person.people[person_name].wife = Person.people[spouse_name]
        if person_data.get("husband"):
            spouse_name = person_data["husband"]
            Person.people[person_name].husband = Person.people[spouse_name]

    return person_objects
