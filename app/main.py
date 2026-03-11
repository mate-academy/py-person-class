class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()
    person_list = [Person(person_dict.get("name"),
                          person_dict.get("age")) for person_dict in people]
    for person_dict in people:
        person = Person.people[person_dict.get("name")]
        partner_wife = person_dict.get("wife")
        partner_husband = person_dict.get("husband")
        if partner_wife:
            person.wife = Person.people[partner_wife]
        elif partner_husband:
            person.husband = Person.people[partner_husband]
    return person_list
