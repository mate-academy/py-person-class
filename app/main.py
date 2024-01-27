class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age

        self.people[self.name] = self


def find_partner(person_obj: Person,
                 person_to_find: str | None
                 ) -> Person | str | None:
    if person_to_find and person_to_find in person_obj.people.keys():
        partner = person_obj.people[person_to_find]
        if hasattr(partner, "wife"):
            partner.wife = person_obj
        elif hasattr(partner, "husband"):
            partner.husband = person_obj
        return person_obj.people[person_to_find]
    else:
        return person_to_find


def create_person_list(people: [dict]) -> [Person]:

    for human_data in people:
        curr_person = Person(human_data["name"], human_data["age"])
        if "wife" in human_data.keys() and human_data["wife"]:
            curr_person.wife = find_partner(curr_person, human_data["wife"])
        elif "husband" in human_data.keys() and human_data["husband"]:
            curr_person.husband = find_partner(curr_person,
                                               human_data["husband"])

    return list(Person.people.values())
