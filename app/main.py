#from tests.test_main import people_data


class Person:
    people = {}
    def __init__(self, name:str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data):
    for person_data in people_data:
        Person(person_data["name"], person_data["age"])

    for person_data in people_data:
        person_instance = Person.people[person_data["name"]]

        if "wife" in person_data and person_data["wife"]:
            person_instance.wife = Person.people[person_data["wife"]]
        elif "husband" in person_data and person_data["husband"]:
            person_instance.husband = Person.people[person_data["husband"]]

    return list(Person.people.values())
