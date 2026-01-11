class Person(object):

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:

    persons = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if person.get("wife") and person["wife"] in Person.people:
            husband_obj = Person.people[person["name"]]
            wife_name = person["wife"]
            husband_obj.wife = Person.people[wife_name]

        elif person.get("husband") and person["husband"] in Person.people:
            wife_obj = Person.people[person["name"]]
            husband_name = person["husband"]
            wife_obj.husband = Person.people[husband_name]

    return persons
