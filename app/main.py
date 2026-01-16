class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    person_list = [
        Person(i.get("name"), i.get("age"))
        for i in people
    ]
    for person_dict, instance in zip(people, person_list):
        partner_name = person_dict.get("wife")
        if partner_name and (partner := Person.people.get(partner_name)):
            instance.wife = partner
        partner_name = person_dict.get("husband")
        if partner_name and (partner := Person.people.get(partner_name)):
            instance.husband = partner
    return person_list
