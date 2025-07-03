class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    persons = [Person(p_dict["name"], p_dict["age"]) for p_dict in people]

    for person_dict in people:
        person = Person.people[person_dict["name"]]

        partner_husband = person_dict.get("husband")
        partner_wife = person_dict.get("wife")

        if partner_husband:
            person.husband = Person.people[partner_husband]
        if partner_wife:
            person.wife = Person.people[partner_wife]
    return persons
