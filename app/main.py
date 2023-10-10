class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    @classmethod
    def couple_create(cls,
                      name: str,
                      partner_name: str,
                      is_male: bool) -> None:
        if partner_name in cls.people and is_male:
            cls.people[name].wife = cls.people[partner_name]
        else:
            cls.people[name].husband = cls.people[partner_name]


def create_person_list(people: list) -> list:
    people_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        person_instance = Person.people[person["name"]]
        if person.get("wife"):
            person_instance.wife = Person.people[person["wife"]]
        elif person.get("husband"):
            person_instance.husband = Person.people[person["husband"]]
    return people_list
