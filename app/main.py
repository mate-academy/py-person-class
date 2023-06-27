class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[self.name] = self


def get_differ(variable_one: str, variable_two: str,
               comparative: list | dict
               ) -> str:
    return variable_one if variable_one in comparative \
        else variable_two if variable_two in comparative else ""


def create_person_list(people: list[dict]) -> list[Person]:
    variable_one, variable_two = "wife", "husband"
    persons = []
    for person in people:
        appended_person = Person(person["name"], person["age"])
        differ = get_differ(variable_one, variable_two,
                            list(person.keys()))
        if differ and person[differ] is not None:
            setattr(appended_person, differ, person[differ])
        persons.append(appended_person)

    for cls_person in persons:
        cls_differ = get_differ(variable_one, variable_two,
                                cls_person.__dict__)
        if cls_differ:
            setattr(cls_person, cls_differ,
                    Person.people.get(cls_person.__dict__[cls_differ]))
    return persons
