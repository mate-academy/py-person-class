class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people = {}
    person_instances_list = []
    for person in people:
        name = person["name"]
        age = person["age"]
        person_obj = Person(name=name, age=age)
        person_instances_list.append(person_obj)
    for person in people:
        current_person_obj = Person.people[person["name"]]
        if "wife" in person and person["wife"] is not None:
            wife_name = person["wife"]
            wife_obj = Person.people[wife_name]
            current_person_obj.wife = wife_obj
        if "husband" in person and person["husband"] is not None:
            husband_name = person["husband"]
            husband_obj = Person.people[husband_name]
            current_person_obj.husband = husband_obj
    return person_instances_list
