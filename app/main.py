class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people_list):

    for person_dict in people_list:
        name = person_dict["name"]
        age = person_dict["age"]
        Person(name, age)

    for person_dict in people_list:
        name = person_dict["name"]
        person_instance = Person.people[name]

        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            person_instance.wife = Person.people[wife_name]

        if "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            person_instance.husband = Person.people[husband_name]

    return [Person.people[person_dict["name"]] for person_dict in people_list]
