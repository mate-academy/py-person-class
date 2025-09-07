class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(name=people_dict["name"], age=people_dict["age"])
                   for people_dict in people]

    for people_dict in people:
        person = Person.people[people_dict["name"]]

        if "wife" in people_dict:
            partner_name = people_dict.get("wife")
            if partner_name:
                person.wife = Person.people[partner_name]

        if "husband" in people_dict:
            partner_name = people_dict.get("husband")
            if partner_name:
                person.husband = Person.people[partner_name]

    return people_list
