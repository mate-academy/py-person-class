class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        self.people[name] = self

    def set_person_partner(self, person: dict) -> None:
        person_partner_type = self.get_person_partner_type(person)
        person_partner_name = person[person_partner_type]

        if person_partner_name is not None:
            setattr(
                self,
                person_partner_type,
                self.people[person_partner_name]
            )

    @staticmethod
    def get_person_partner_type(person: dict) -> str:
        for key in person.keys():
            if key == "wife" or key == "husband":
                return key


def create_person_list(people: list) -> list:
    people_inst_list = []

    for person in people:
        person_inst = Person(person["name"], person["age"])
        people_inst_list.append(person_inst)

    for i in range(len(people_inst_list)):
        person_inst = people_inst_list[i]
        person_inst.set_person_partner(people[i])

    return people_inst_list
