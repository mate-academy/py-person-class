class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age

        Person.people[self.name] = self


def find_partner_and_set_his_partner(
    person_obj: Person,
    person_to_find: str | None
) -> Person | None:
    if person_to_find in Person.people:
        partner = Person.people[person_to_find]
        if hasattr(partner, "wife"):
            partner.wife = person_obj
        elif hasattr(partner, "husband"):
            partner.husband = person_obj
        return partner


def create_person_list(people: list[dict]) -> list[Person]:
    created_items = []
    for human_data in people:
        curr_person = Person(human_data["name"], human_data["age"])
        created_items.append(curr_person)
        set_partner(curr_person, human_data)
    return created_items


def set_partner(person: Person, person_data: dict) -> None:
    if person_data.get("wife"):
        person.wife = find_partner_and_set_his_partner(
            person,
            person_data["wife"]
        )
    elif person_data.get("husband"):
        person.husband = find_partner_and_set_his_partner(
            person,
            person_data["husband"]
        )
