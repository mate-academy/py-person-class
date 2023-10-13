class Person:
    people = {}

    def __init__(self, name: str = "", age: int = 0) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_dict = Person.people
    for person in people:
        person_name = person["name"]
        person_age = person["age"]
        spouse = "wife" if "wife" in list(person.keys()) else "husband"
        spouse_name = person[spouse]

        if person_name not in people_dict:
            Person(person_name, person_age)

        if spouse_name:
            setattr(people_dict[person_name], spouse, spouse_name)

    for person, obj in people_dict.items():
        spouse = [s for s in obj.__dict__ if s in ["wife", "husband"]]
        if not spouse:
            continue
        spouse_name = obj.__dict__[spouse[0]]
        setattr(people_dict[person], spouse[0], people_dict[spouse_name])

    return [person_obj for person_obj in people_dict.values()]
