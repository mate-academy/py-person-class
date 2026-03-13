class Person:
    people ={}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    person_inst = []
    for person in people:
        name = person["name"]
        age = person["age"]
        new_person = Person(name, age)
        person_inst.append(new_person)
    for i in range(len(people)):
        person_data = people[i]
        person_data_from_person_inst = person_inst[i]
        if "wife" in person_data and person_data["wife"] is not None:
            wife_name = person_data["wife"]
            person_data_from_person_inst.wife = Person.people[wife_name]
        if "husband" in person_data and person_data["husband"] is not None:
            husband_name = person_data["husband"]
            person_data_from_person_inst.husband = Person.people[husband_name]
    return person_inst


