class Person:

    people = {}

    def __init__(self, name: "str", age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})

    def add_partner(self, partner_name: str) -> None:
        self.partner = Person.people[partner_name]


def create_person_list(people: list) -> list:

    people_list = []
    for person in people:
        new_obj = Person(person["name"], person["age"])
        try:
            if person["wife"] is not None:
                new_obj.wife = person["wife"]
        except (KeyError, AttributeError):
            if person["husband"] is not None:
                new_obj.husband = person["husband"]
        people_list.append(new_obj)
    for obj in people_list:
        try:
            partner = Person.people[obj.wife]
            delattr(obj, "wife")
            setattr(obj, "wife", partner)
        except (KeyError, AttributeError):
            try:
                partner = Person.people[obj.husband]
                delattr(obj, "husband")
                setattr(obj, "husband", partner)
            except (KeyError, AttributeError):
                continue

    return people_list
