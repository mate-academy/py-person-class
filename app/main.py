class Person:
    people = {}

    def __init__(self, name: str, age: str) -> Person:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: dict) -> Person:
    Person.people.clear()
    person_list = [Person(peoples["name"],
                          peoples["age"]) for peoples in people]
    for peoples in people:
        person = Person.people[peoples["name"]]
        partner_wife = peoples.get("wife")
        partner_husband = peoples.get("husband")
        if partner_wife:
            person.wife = Person.people[partner_wife]
        elif partner_husband:
            person.husband = Person.people[partner_husband]
    return person_list
