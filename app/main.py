class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]
    for person in people:
        person_name = person["name"]
        person_object = Person.people[person_name]
        if person.get("wife") is not None:
            person_wife = person["wife"]
            wife_object = Person.people[person_wife]
            person_object.wife = wife_object
        if person.get("husband") is not None:
            person_husband = person["husband"]
            husband_object = Person.people[person_husband]
            person_object.husband = husband_object
    return person_list
