class Person:
    people = {}
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self



def create_person_list(people: list) -> list:
    person_list = []
    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        person_list.append(Person(name, age))

    for person_dict in people:
        person_item = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"]:
            person_item.wife = Person.people[person_dict["wife"]]
        if "husband" in person_dict and person_dict["husband"]:
            person_item.husband = Person.people[person_dict["husband"]]

    return person_list

