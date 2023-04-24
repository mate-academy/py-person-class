class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    @classmethod
    def sett_partner(cls, human: dict) -> None:
        person_name = human.get("name")
        wife_name = human.get("wife")
        husband_name = human.get("husband")

        if wife_name:
            cls.people[person_name].wife = cls.people[wife_name]
        if husband_name:
            cls.people[person_name].husband = cls.people[husband_name]

    @classmethod
    def get_person_obj_list(cls) -> list:
        return list(cls.people.values())


def create_person_list(people: list) -> list:
    [Person(person.get("name"), person.get("age")) for person in people]
    [Person.sett_partner(person) for person in people]
    return Person.get_person_obj_list()
