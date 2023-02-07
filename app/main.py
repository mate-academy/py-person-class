class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        name = person["name"]
        age = person["age"]
        if name not in Person.people:
            person_obj = Person(name, age)
        else:
            person_obj = Person.people[name]
        if "wife" in person:
            wife_name = person["wife"]
            if wife_name is not None:
                if wife_name not in Person.people:
                    wife = Person(wife_name, None)
                else:
                    wife = Person.people[wife_name]
                person_obj.wife = wife
        if "husband" in person:
            husband_name = person["husband"]
            if husband_name is not None:
                if husband_name not in Person.people:
                    husband = Person(husband_name, None)
                else:
                    husband = Person.people[husband_name]
                person_obj.husband = husband
        person_list.append(person_obj)
    return person_list
