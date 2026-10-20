class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_person = []
    for index, person in enumerate(people):
        person_obj = Person(person["name"], person["age"])
        if person.get("wife"):
            person_obj.wife = person["wife"]
        if person.get("husband"):
            person_obj.husband = person["husband"]
        list_person.append(person_obj)
    for person in list_person:
        if hasattr(person, "wife"):
            person.wife = Person.people.get(person.wife)
        if hasattr(person, "husband"):
            person.husband = Person.people.get(person.husband)

    return list_person
