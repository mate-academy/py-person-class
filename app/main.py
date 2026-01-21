class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = [
        Person(person_info["name"], person_info["age"])
        for person_info in people
    ]

    for person_instance, person_info in zip(person_instances, people):
        if person_info.get("wife") is not None:
            partner_name = person_info.get("wife")
            person_instance.wife = Person.people.get(partner_name)

        if person_info.get("husband") is not None:
            partner_name = person_info.get("husband")
            person_instance.husband = Person.people.get(partner_name)

    return person_instances
