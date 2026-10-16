
class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    person_list = []

    for person in people:
        person_obj = Person(person["name"], person["age"])
        person_list.append(person_obj)

    for person_dict, person_obj in zip(people, person_list):
        for key in ("wife", "husband"):
            relative_name = person_dict.get(key)

            if relative_name is not None:
                setattr(person_obj, key, Person.people[relative_name])

    return person_list
