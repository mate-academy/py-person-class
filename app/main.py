class Person:
    people = {}  # Class attribute to store Person instances by their name

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list :
    person_instances = [
        Person(person_data["name"], person_data["age"])
        for person_data in people_list
    ]

    for person_instance, person_data in zip(person_instances, people_list):
        if person_data.get("wife"):
            partner_name = person_data.get("wife")
            person_instance.wife = Person.people.get(partner_name)

        if person_data.get("husband"):
            partner_name = person_data.get("husband")
            person_instance.husband = Person.people.get(partner_name)

    return person_instances
