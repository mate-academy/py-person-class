class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    for person_dict in people:
        Person(person_dict["name"], person_dict["age"])

    for person_dict in people:
        person_obj = Person.people[person_dict["name"]]

        if "wife" in person_dict and person_dict["wife"]:
            wife_name = person_dict["wife"]
            if wife_name in Person.people:
                person_obj.wife = Person.people[wife_name]

        elif "husband" in person_dict and person_dict["husband"]:
            husband_name = person_dict["husband"]
            if husband_name in Person.people:
                person_obj.husband = Person.people[husband_name]

    return [Person.people[p["name"]] for p in people]
