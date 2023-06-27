class Person:
    people: dict[str, "Person"] = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(list_people: list[dict]) -> list[Person]:
    people_list = [Person(person_dict["name"],
                          person_dict["age"]) for person_dict in list_people]

    for person_dict in list_people:
        if "husband" in person_dict and person_dict["husband"] is not None:
            curr_person_name: str = person_dict["name"]
            husband_name: str = person_dict["husband"]
            curr_person = Person.people[curr_person_name]
            husband_person = Person.people[husband_name]
            curr_person.husband = husband_person

        elif "wife" in person_dict and person_dict["wife"] is not None:
            curr_person_name: str = person_dict["name"]
            wife_name: str = person_dict["wife"]
            curr_person = Person.people[curr_person_name]
            wife_person = Person.people[wife_name]
            curr_person.wife = wife_person

    return people_list
