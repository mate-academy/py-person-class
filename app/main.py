class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:

    persons_dict = {person_data["name"]: Person(person_data["name"],
                                                person_data["age"])
                    for person_data in people}

    for person_data in people:
        name = person_data["name"]
        if "wife" in person_data and person_data["wife"]:
            wife_name = person_data["wife"]
            persons_dict[name].wife = persons_dict.get(wife_name, None)
        elif "husband" in person_data and person_data["husband"]:
            husband_name = person_data["husband"]
            persons_dict[name].husband = persons_dict.get(husband_name, None)

    return list(persons_dict.values())
