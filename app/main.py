class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []
    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        person = Person(name, age)
        person_instances.append(person)
    for person_dict in people:
        person = Person.people[person_dict["name"]]
        husband_name = person_dict.get("husband")
        wife_name = person_dict.get("wife")
        if husband_name:
            person.husband = Person.people[husband_name]
        if wife_name:
            person.wife = Person.people[wife_name]

    return person_instances
