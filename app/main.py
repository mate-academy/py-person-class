class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    person_inst = [Person(person["name"], person["age"]) for person in people]

    for i in range(len(people)):
        person_data = people[i]
        data_person_inst = person_inst[i]
        wife_name = person_data.get("wife")
        if wife_name:
            data_person_inst.wife = Person.people[wife_name]
        husband_name = person_data.get("husband")
        if husband_name:
            data_person_inst.husband = Person.people[husband_name]

    return person_inst
