class Person:

    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:

    list_of_person_objects = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for ind, person in enumerate(people):
        if list(person.values())[-1] is not None:
            spouse_status = list(person.keys())[-1]
            spouse_name = list(person.values())[-1]

            if spouse_name in list(Person.people.keys()):
                ind_spouse = list(Person.people.keys()).index(spouse_name)
                setattr(list_of_person_objects[ind],
                        spouse_status,
                        list_of_person_objects[ind_spouse])

    return list_of_person_objects
