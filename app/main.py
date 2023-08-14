class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people):
    person_list = []

    name_to_instance = {}

    for person_info in people:
        name = person_info["name"]
        age = person_info["age"]

        person_list.append(Person(name, age))
        name_to_instance[name] = Person(name, age)

    for person_info in people:
        name = person_info["name"]
        spouse_name = person_info.get("wife") or person_info.get("husband")

        if spouse_name:
            person_instance = name_to_instance[name]
            spouse_instance = name_to_instance[spouse_name]
            person_instance.spouse = spouse_instance
            spouse_instance.spouse = person_instance

    return person_list
