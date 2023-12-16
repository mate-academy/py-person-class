class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self

def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    
    for person in people:
        for partner_type in ["wife", "husband"]:
            if partner_type in person and person[partner_type] is not None:
                person_object = Person.people[person["name"]]
                partner_object = Person.people[person[partner_type]]
                setattr(person_object, partner_type, partner_object)
    
    return person_list
