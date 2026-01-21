class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people: list) -> list:
    list_person = []

    for person in people:
        Person(person["name"], person["age"])

    for person2 in people:
        spouse_name = Person.people[person2.get("name")]
        if person2.get("wife") is not None:
            spouse_name.wife = Person.people[person2.get("wife")]
        if person2.get("husband") is not None:
            spouse_name.husband = Person.people[person2.get("husband")]
        list_person.append(spouse_name)
    return list_person
