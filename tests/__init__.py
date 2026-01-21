class Person:
    people = {}
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self

def create_person_list(people_dict: list) -> list:
    person_list = [Person(person['name'], person['age']) for person in people_dict]

    for person in people_dict:
        current_person = Person.people[person["name"]]

        wife_name = person.get("wife")
        if wife_name is not None:
            current_person.wife = Person.people[wife_name]

        husband_name = person.get("husband")
        if husband_name is not None:
            current_person.husband = Person.people[husband_name]

    return person_list




