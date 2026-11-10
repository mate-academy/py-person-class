class Person:
    people = {}
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.husband = None
        self.wife = None


def create_person_list(people_data: list) -> list:
    person_list = []
    for data in people_data:
        name = data["name"]
        age = data["age"]
        person = Person(name, age)
        person_list.append(person)

    for data in people_data:
        person = Person.people[data["name"]]
        if "wife" in data and data["wife"] is not None:
            perspn.wife = Person.people[data["wife"]]

        elif "husband" in data and data["husband"] is not None:
            perspn.husband = Person.people[data["husband"]]

    return person_list





