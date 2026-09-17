class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person_dict in people:
        result.append(Person(person_dict["name"], person_dict["age"]))

    for person_dict in people:
        person_obj = Person.people[person_dict["name"]]

        if person_dict.get("wife") is not None:
            wife_name = person_dict["wife"]
            person_obj.wife = Person.people[wife_name]

        if person_dict.get("husband") is not None:
            husband_name = person_dict["husband"]
            person_obj.husband = Person.people[husband_name]

    return result
