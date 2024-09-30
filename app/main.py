class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        if "wife" in person and person["wife"]:
            partner_name = person["wife"]
            partner_type = "wife"
        elif "husband" in person and person["husband"]:
            partner_name = person["husband"]
            partner_type = "husband"
        else:
            partner_name = None
            partner_type = None
        person_instance = Person(person["name"], person["age"])
        person_instance.partner_name = partner_name
        person_instance.partner_type = partner_type
        person_list.append(person_instance)
    for person in person_list:
        if person.partner_name:
            partner = Person.people[person.partner_name]
            if person.partner_type == "wife":
                person.wife = partner
                partner.husband = person
            elif person.partner_type == "husband":
                person.husband = partner
                partner.wife = person
    return person_list
