class Person:
    people = {}


    def __init__(self, name , age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_objects  = [Person(p["name"], p["age"]) for p in people]

    for key , value in zip(people, person_objects ):
        partner_wife = key.get("wife")
        partner_husband = key.get("husband")

        if partner_wife is not None and partner_wife != "":
            if partner_wife in Person.people:
                value.wife = Person.people[partner_wife]
            else:
                raise AttributeError(KeyError)
        if partner_husband is not None and partner_husband != "":
            if partner_husband in Person.people:
                value.husband = Person.people[partner_husband]
            else:
                raise AttributeError(KeyError)

    return person_objects


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]

person_list = create_person_list(people)
print(person_list)
