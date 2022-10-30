class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people.update({self.name: self})


def create_person_list(people: list) -> list:
    list_of_person_instances = [Person(person["name"],
                                       person["age"]) for person in people]

    for person in people:
        partner_type = [*person.keys()][2]
        partner_name = person[partner_type]
        person_name = person["name"]
        if partner_name is not None:
            if partner_type == "wife":
                Person.people[person_name].wife = Person.people[partner_name]
            Person.people[person_name].husband = Person.people[partner_name]

    return list_of_person_instances
