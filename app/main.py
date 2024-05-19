class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.add_person_to_people(self)

    @classmethod
    def add_person_to_people(cls, person) -> None:
        cls.people[person.name] = person


def create_person_list(people: list) -> list:
    result = []
    for person_dict in people:
        person_obj = Person(person_dict["name"], person_dict["age"])
        result.append(person_obj)

    name_obj = Person.people
    for person_dict in people:
        person_obj = name_obj[person_dict["name"]]

        if person_dict.get("wife") is not None:
            person_obj.wife = name_obj[person_dict["wife"]]

        if person_dict.get("husband") is not None:
            person_obj.husband = name_obj[person_dict["husband"]]

    return result
