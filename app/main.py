class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(p["name"], p["age"]) for p in people]

    for person_dict in people:
        if person_dict.get("wife") is not None:
            wife_name = person_dict.get("wife")
            husband_name = person_dict.get("name")

            husband_obj = Person.people[husband_name]
            wife_obj = Person.people[wife_name]

            husband_obj.wife = wife_obj

        elif person_dict.get("husband") is not None:
            husband_name = person_dict.get("husband")
            wife_name = person_dict.get("name")

            husband_obj = Person.people[husband_name]
            wife_obj = Person.people[wife_name]

            wife_obj.husband = husband_obj

    return person_list
