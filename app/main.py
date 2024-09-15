class Person:
    people = {}
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self
def create_person_list(people: list) -> list:
    new_people_list = []
    wife = "wife"
    husband = "husband"

    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        person_obj = Person.people[person["name"]]
        partner = person.get(wife) or person.get(husband) or None
        partner_obj = None

        if partner:
            partner_obj = person_obj.people.get(partner)

        if person.get(wife):
            person_obj.wife = partner_obj
        elif person.get(husband):
            person_obj.husband = partner_obj

        new_people_list.append(person_obj)

    return new_people_list
