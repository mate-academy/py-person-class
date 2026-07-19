class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        Person.people[name] = self
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    people_list_with_wife_or_husband = []
    for person in people:
        person_name = person["name"]
        person_age = person["age"]
        Person(person_name, person_age)

    for person in people:
        if "wife" in person and person["wife"] is not None:
            person_name = person["name"]
            wife_instance = Person.people[person["wife"]]
            Person.people[person_name].wife = wife_instance

        if "husband" in person and person["husband"] is not None:
            person_name = person["name"]
            husband_instance = Person.people[person["husband"]]
            Person.people[person_name].husband = husband_instance

    for person in Person.people.values():
        people_list_with_wife_or_husband.append(person)

    names_order = [person["name"] for person in people]
    people_list_with_wife_or_husband.sort(
        key=lambda x: names_order.index(x.name)
    )
    return people_list_with_wife_or_husband
