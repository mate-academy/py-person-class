class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people.update({name: self})


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        result.append(new_person)
    for person_date in people:
        person = Person.people[person_date["name"]]
        if "wife" in person_date and person_date["wife"]:
            person.wife = Person.people.get(person_date["wife"])
        if "husband" in person_date and person_date["husband"]:
            person.husband = Person.people.get(person_date["husband"])
    return result
