class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        self.people[name] = self


def create_person_list(people_data: list) -> list:
    people = []
    for person_dict in people_data:
        name = person_dict.get("name")
        age = person_dict.get("age")
        person = Person(name, age)

        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict.get("wife")
            if wife_name in Person.people:
                person.wife = Person.people[wife_name]
                Person.people[wife_name].husband = person

        if hasattr(person, "wife") and person.wife is None:
            del person.wife

        if "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict.get("husband")
            if husband_name in Person.people:
                person.husband = Person.people[husband_name]
                Person.people[husband_name].wife = person

        people.append(person)

    return people
