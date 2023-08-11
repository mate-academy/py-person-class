class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def set_wife(self, wife: str) -> None:
        self.wife = wife

    def set_husband(self, husband: str) -> None:
        self.husband = husband


def create_person_list(people_list: list) -> list:
    result = []

    for person_dict in people_list:
        name = person_dict["name"]
        age = person_dict["age"]
        result.append(Person(name, age))

    name_to_person = {person.name: person for person in result}

    for person in result:
        person_dict = next(p for p in people_list if p["name"] == person.name)

        wife_name = person_dict.get("wife")
        if wife_name:
            wife_instance = name_to_person.get(wife_name)
            if wife_instance:
                person.set_wife(wife_instance)

        husband_name = person_dict.get("husband")
        if husband_name:
            husband_instance = name_to_person.get(husband_name)
            if husband_instance:
                person.set_husband(husband_instance)

    return result
