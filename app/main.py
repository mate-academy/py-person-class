class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_instances = [
        Person(name=person_dict["name"], age=person_dict["age"])
        for person_dict in people
    ]

    for person_dict in people:
        person_obj = Person.people[person_dict["name"]]

        if person_dict.get("wife"):
            wife_name = person_dict["wife"]
            person_obj.wife = Person.people[wife_name]

        if person_dict.get("husband"):
            husband_name = person_dict["husband"]
            person_obj.husband = Person.people[husband_name]

    return person_instances
