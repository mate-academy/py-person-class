class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None     :
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    result = [
        Person(person_data["name"],
               person_data["age"])
        for person_data in people
    ]

    for person_data in people:
        current_instance = Person.people[person_data["name"]]

        partner_key = "wife" if person_data.get("wife") else "husband"
        partner_name = person_data.get(partner_key)
        if partner_name is not None:
            setattr(current_instance, partner_key, Person.people[partner_name])

    return result
