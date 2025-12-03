class Person:
    people = {}


    def __init__(self, name , age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    person_objects  = [Person(p["name"], p["age"]) for p in people]

    for person_dict , person_object in zip(people, person_objects ):
        partner_wife = person_dict.get("wife")
        partner_husband = person_dict.get("husband")


        if partner_wife and partner_wife in Person.people:
            person_object.wife = Person.people[partner_wife]
        else:
            raise ValueError(f"Person with name '{partner_wife}' not found")
        if partner_husband and partner_husband in Person.people:
            person_object.husband = Person.people[partner_husband]
        else:
            raise ValueError(f"Person with name '{partner_husband}' not found")


    return person_objects