class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_dict = {person["name"]: Person(person["name"],
                                          person["age"]) for person in people}

    for person in people:
        person_obj = person_dict[person["name"]]
        wife_name = person.get("wife")
        husband_name = person.get("husband")

        if wife_name:
            person_obj.wife = person_dict.get(wife_name)
        if husband_name:
            person_obj.husband = person_dict.get(husband_name)

    return list(person_dict.values())
