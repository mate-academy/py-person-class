class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        self.__class__.people[name] = self

    def __setattr__(self, name, value):
        if name == "wife" and value is None:
            return
        if name == "husband" and value is None:
            return
        super().__setattr__(name, value)


def create_person_list(people):
    person_list = []
    for person in people:
        name = person["name"]
        age = person["age"]
        p = Person(name, age)
        if "wife" in person and person["wife"] is not None:
            wife_name = person["wife"]
            if wife_name in Person.people:
                p.wife = Person.people[wife_name]
                Person.people[wife_name].husband = p
        elif "husband" in person and person["husband"] is not None:
            husband_name = person["husband"]
            if husband_name in Person.people:
                p.husband = Person.people[husband_name]
                Person.people[husband_name].wife = p
        person_list.append(p)
    return person_list
