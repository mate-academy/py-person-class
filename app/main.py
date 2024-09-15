class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        self.people[name] = self


def create_person_list(people: list) -> list:
    new_list_of_people = []

    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        person_obj = Person.people[person["name"]]
        partner_name = person.get("wife") or person.get("husband") or None
        partner_obj = None

        if partner_name:
            partner_obj = person_obj.people.get(partner_name)

        if person.get("wife"):
            person_obj.wife = partner_obj
        elif person.get("husband"):
            person_obj.husband = partner_obj

        new_list_of_people.append(person_obj)

    return new_list_of_people
