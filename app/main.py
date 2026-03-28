class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    [Person(person_data["name"], person_data["age"]) for person_data in people]
    for person_data in people:
        person_inst = Person.people[person_data["name"]]
        wife_name = person_data.get("wife")
        if wife_name:
            person_inst.wife = Person.people[wife_name]
        husband_name = person_data.get("husband")
        if husband_name:
            person_inst.husband = Person.people[husband_name]
    return [Person.people[person_data["name"]] for person_data in people]
