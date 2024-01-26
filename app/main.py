class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age

        self.people[self.name] = self


def find_partner(obj: Person,
                 person_to_find: str | None
                 ) -> Person | str | None:
    if person_to_find and person_to_find in obj.people.keys():
        partner = obj.people[person_to_find]
        if hasattr(partner, "wife") and partner.wife == obj.name:
            partner.wife = obj
        elif hasattr(partner, "husband") and partner.husband == obj.name:
            partner.husband = obj
        return obj.people[person_to_find]
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

tmp = [
        {"name": "Ross", "age": 30, "wife": "Rachel"},
        {"name": "Joey", "age": 29, "wife": None},
        {"name": "Phoebe", "age": 31, "husband": None},
        {"name": "Chandler", "age": 30, "wife": "Monica"},
        {"name": "Monica", "age": 32, "husband": "Chandler"},
        {"name": "Rachel", "age": 28, "husband": "Ross"},
    ]

created_person_list = create_person_list(tmp)

print(hasattr(created_person_list[0], "wife"))
print(created_person_list[0].wife.husband == created_person_list[0])
print(hasattr(created_person_list[1], "wife") is False)
