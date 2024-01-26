from __future__ import annotations


class Person:
    people = {}  # people collection, key=name, value = ref to a person

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age

        Person.people[self.name] = self


def find_partner(obj: Person,
                 person_to_find: str | None
                 ) -> Person | str | None:
    # if the person exists
    if person_to_find and person_to_find in obj.people.keys():
        partner = obj.people[person_to_find]
        # write this person as a partner`s partner
        if hasattr(partner, "wife") and partner.wife == obj.name:
            partner.wife = obj
        elif hasattr(partner, "husband") and partner.husband == obj.name:
            partner.husband = obj
        return obj.people[person_to_find]
    else:  # return str if partner non exists
        return person_to_find


def create_person_list(people: [dict]) -> [Person]:

    for human_data in people:
        curr_person = Person(human_data["name"], human_data["age"])
        if "wife" in human_data.keys():
            curr_person.wife = find_partner(curr_person, human_data["wife"])
        elif "husband" in human_data.keys():
            curr_person.husband = find_partner(curr_person,
                                               human_data["husband"])

    return list(Person.people.values())
