class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person_dict in people:
        Person(person_dict["name"], person_dict["age"])

    for person_dict in people:
        name = person_dict["name"]
        person_instance = Person.people[name]

        if person_dict.get("wife"):
            wife_name = person_dict["wife"]
            person_instance.wife = Person.people[wife_name]

        if person_dict.get("husband"):
            husband_name = person_dict["husband"]
            person_instance.husband = Person.people[husband_name]

    return list(Person.people.values())
