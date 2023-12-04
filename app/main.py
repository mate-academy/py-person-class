class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # ----------------------------listing dict -> personalization
    ls = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]
    # ----------------------------check for partner
    for person_data in people:
        person_data_instance = Person.people[person_data["name"]]
        partner_name = person_data.get("wife") or person_data.get("husband")
    # ----------------------------add a partner depending on
        if partner_name:
            partner_instance = Person.people.get(partner_name)
            if partner_instance:
                if "wife" in person_data:
                    person_data_instance.wife = partner_instance
                elif "husband" in person_data:
                    person_data_instance.husband = partner_instance

    return ls
