class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_persons = [
        Person(person["name"], person["age"]) for person in people
    ]
    for link_to_people, link_to_persons in zip(people, list_of_persons):
        partner_name_wife = link_to_people.get("wife")
        partner_name_husband = link_to_people.get("husband")
        if partner_name_wife is not None:
            setattr(link_to_persons, "wife", Person.people[partner_name_wife])
        if partner_name_husband is not None:
            setattr(
                link_to_persons, "husband", Person.people[partner_name_husband]
            )
    return list_of_persons
