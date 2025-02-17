class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self

    def __repr__(self):
        return f"<Person name={self.name}, age={self.age}>"


def create_person_list(people_data):
    person_list = []

    for person_dict in people_data:
        name = person_dict["name"]
        age = person_dict["age"]
        person = Person(name, age)
        person_list.append(person)

    for person_dict, person in zip(people_data, person_list):
        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            person.wife = Person.people[wife_name]
        elif "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            person.husband = Person.people[husband_name]

    return person_list
