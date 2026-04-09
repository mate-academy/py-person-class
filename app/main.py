class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    Person.people = {}

    for p_dict in people_data:
        Person(p_dict["name"], p_dict["age"])

    person_instances = []

    for p_dict in people_data:
        name = p_dict["name"]
        person_obj = Person.people[name]

        if p_dict.get("wife"):
            wife_name = p_dict["wife"]
            person_obj.wife = Person.people[wife_name]

        if p_dict.get("husband"):
            husband_name = p_dict["husband"]
            person_obj.husband = Person.people[husband_name]

        person_instances.append(person_obj)

    return person_instances
