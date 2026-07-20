class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person_dict, person_instance in zip(people, person_list):
        partner_name = person_dict.get("wife") or person_dict.get("husband")

        if partner_name is not None:
            partner_instance = Person.people[partner_name]

            if "wife" in person_dict:
                person_instance.wife = partner_instance
            else:
                person_instance.husband = partner_instance

    return person_list
