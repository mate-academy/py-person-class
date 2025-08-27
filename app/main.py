class Person:

    people = {}
    people_data = []

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

def create_person_list(people_data: list) -> list:
    person_list = []
    for person_dict in people_data:
        person_object = Person(person_dict["name"], person_dict["age"])
        person_list.append(person_object)
    return person_list

    for person_dict in people_data:
        current_person = Person.people[person_dict["name"]]
        if "husband" in person_dict:
            current_person.husband = Person.people[person_dict["husband"]]
        if "wife" in person_dict:
            current_person.wife = Person.people[person_dict["wife"]]






