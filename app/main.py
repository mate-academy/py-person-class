class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people):
    Person.people.clear()

    person_list = [
        Person(person_dict.get("name"), person_dict.get("age"))
        for person_dict in people
    ]

    for person_dict in people:
        person = Person.people.get(person_dict.get("name"))

        wife_name = person_dict.get("wife")
        if wife_name is not None:
            spouse = Person.people.get(wife_name)
            if spouse:
                person.wife = spouse

        husband_name = person_dict.get("husband")
        if husband_name is not None:
            spouse = Person.people.get(husband_name)
            if spouse:
                person.husband = spouse

    return person_list