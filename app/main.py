class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person_dict["name"],
                          person_dict["age"])
                   for person_dict in people]

    # wife/husband
    for person_dict in people:
        current_person = Person.people[person_dict["name"]]

        if person_dict.get("wife") is not None:
            wife_name = person_dict["wife"]
            current_person.wife = Person.people[wife_name]

        if person_dict.get("husband") is not None:
            husband_name = person_dict["husband"]
            current_person.husband = Person.people[husband_name]

    return person_list
