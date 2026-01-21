class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(p["name"], p["age"]) for p in people]
    for person_dict in people:
        person = Person.people[person_dict["name"]]

        male_value = person_dict.get("husband")
        female_value = person_dict.get("wife")
        if male_value is not None:
            husband_name = person_dict["husband"]
            person.husband = Person.people[husband_name]

        elif female_value is not None:
            wife_name = person_dict["wife"]
            person.wife = Person.people[wife_name]

    return people_list
