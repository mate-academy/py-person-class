class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = list()
    for person_info in people:
        person_entry = Person(name=person_info["name"], age=person_info["age"])
        partner_status, partner_name = None, None
        if "wife" in person_info:
            partner_name = person_info["wife"]
            partner_status = "wife"
        elif "husband" in person_info:
            partner_name = person_info["husband"]
            partner_status = "husband"
        if partner_status is not None and partner_name in Person.people:
            partner_entry = Person.people.get(partner_name)
            if partner_status == "wife":
                person_entry.wife = partner_entry
                partner_entry.husband = person_entry
            else:
                person_entry.husband = partner_entry
                partner_entry.wife = person_entry

        people_list.append(person_entry)

    return people_list
