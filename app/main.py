class Person:
    people: dict[str, "Person"] = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(list_people: list[dict]) -> list[Person]:
    people_list = [Person(person_dict["name"],
                          person_dict["age"]) for person_dict in list_people]

    for person_dict in list_people:
        if person_dict.get("husband") is not None:
            curr_person = Person.people[person_dict["name"]]
            husband = Person.people[person_dict["husband"]]
            curr_person.husband = husband

        elif person_dict.get("wife") is not None:
            curr_person = Person.people[person_dict["name"]]
            wife = Person.people[person_dict["wife"]]
            curr_person.wife = wife

    return people_list
