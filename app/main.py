class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    wife_and_husband = {}
    result = []

    for person in people:
        result.append(Person(
            person["name"],
            person["age"]
        ))
        if "husband" in person and person["husband"] is not None:
            wife_and_husband[person["name"]] = person["husband"]

    for wife in wife_and_husband:
        wife_name = Person.people[wife]
        husband_name = Person.people[wife_and_husband[wife]]

        wife_name.husband = husband_name
        husband_name.wife = wife_name
    return result
