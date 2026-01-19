class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(name=person["name"],
                          age=person["age"]) for person in people]

    def get_partner_pointer(partner_name: str) -> Person:
        nonlocal person_list
        for person in person_list:
            if person.name == partner_name:
                return person

    for i in range(len(person_list)):
        person = person_list[i]
        pair_name = people[i].get("wife")
        if pair_name:
            person.wife = get_partner_pointer(pair_name)
        elif people[i].get("husband"):
            person.husband = get_partner_pointer(people[i].get("husband"))

    return person_list
