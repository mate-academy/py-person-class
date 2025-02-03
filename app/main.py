class Person:
    people = {}
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self



def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person_dict in people:
        person_item = Person.people[person_dict["name"]]
        wife_name = person_dict.get("wife")
        husband_name = person_dict.get("husband")

        if wife_name and wife_name in Person.people:
            person_item.wife = Person.people[wife_name]

        if husband_name and husband_name in Person.people:
            person_item.husband = Person.people[husband_name]

    return person_list

