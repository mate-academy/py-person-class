class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    result = []
    for person_dict in people_data:
        person = Person(person_dict["name"], person_dict["age"])
        result.append(person)
    for person_dict in people_data:

        person = Person.people[person_dict["name"]]

        if "wife" in person_dict and person_dict["wife"]:
            person.wife = Person.people[person_dict.get(["wife"])]

        if "husband" in person_dict and person_dict.get(["husband"]):
            person.husband = Person.people[person_dict["husband"]]
    return result
