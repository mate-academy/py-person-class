class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        name, age, partner_name = person.values()
        if name not in Person.people:
            instance = Person(name, age)
            Person.people[name] = instance
            if person.get("wife") or person.get("husband"):
                for partner in people:
                    partner_real_name, partner_age, *_ = partner.values()
                    if partner_name == partner_real_name:
                        if "wife" in person:
                            new_instance = Person(partner_real_name,
                                                  partner_age)
                            instance.wife = new_instance
                            new_instance.husband = instance
                        else:
                            new_instance = Person(partner_real_name,
                                                  partner_age)
                            instance.husband = new_instance
                            new_instance.wife = instance
        else:
            instance = Person.people.get(name)
        result.append(instance)
    return result
