class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self

def create_person_list(people: list) -> list:
    Person.people.clear()
    [Person(person["name"], person["age"]) for person in people]
    for person in people:
        person_obj = Person.people[person["name"]]
        wife_name = person.get("wife")
        if wife_name is not None:
            person_obj.wife = Person.people[wife_name]
        husband_name = person.get("husband")
        if husband_name is not None:
            person_obj.husband = Person.people[husband_name]
    return [Person.people[person["name"]] for person in people]
