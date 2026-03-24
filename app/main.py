class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    persons_list = []
    for person in people:
        persons_list = [Person(p["name"], p["age"]) for p in people]

    for idx, person_dict in enumerate(people):
        wife_name = person_dict.get("wife")
        if wife_name:
            spouse = Person.people.get(wife_name)
            if spouse is None:
                raise KeyError(f"Unknown wife name: {wife_name}")
            persons_list[idx].wife = spouse

        husband_name = person_dict.get("husband")
        if husband_name:
            spouse = Person.people.get(husband_name)
            if spouse is None:
                raise KeyError(f"Unknown husband name: {husband_name}")
            persons_list[idx].husband = spouse
    return persons_list
