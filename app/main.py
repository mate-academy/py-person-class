
class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    @classmethod
    def sett_partner(cls, human: dict) -> None:
        person_data = [(key, value) for key, value in human.items()]
        person_name = person_data[0][1]
        partner_role = person_data[2][0]
        partner_name = person_data[2][1]

        if partner_name:
            if partner_role == "wife":
                cls.people[person_name].wife = cls.people[partner_name]
            if partner_role == "husband":
                cls.people[person_name].husband = cls.people[partner_name]

    @classmethod
    def get_person_obj_list(cls) -> list:
        return list(cls.people.values())


def create_person_list(people: list) -> list:
    [Person(name=person.get("name"), age=person.get("age"))
     for person in people]
    [[Person.sett_partner(person)
     for key, value in person.items() if value is not None]
     for person in people]
    return Person.get_person_obj_list()
