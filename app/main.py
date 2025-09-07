class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for one_people in people:
        person = Person(name=one_people["name"], age=one_people["age"])
        people_list.append(person)

    for one_people in people:
        person = Person.people[one_people["name"]]

        if "wife" in one_people and one_people["wife"] is not None:
            partner_name = one_people["wife"]
            partner = Person.people[partner_name]
            person.wife = partner

        if "husband" in one_people and one_people["husband"] is not None:
            partner_name = one_people["husband"]
            partner = Person.people[partner_name]
            person.husband = partner

    return people_list
