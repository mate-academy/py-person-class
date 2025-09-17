class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    instances = [Person(d["name"], d["age"]) for d in people]

    for person in people:
        wife_name = person.get("wife")
        if wife_name:
            main_obj = Person.people[person["name"]]
            spouse_obj = Person.people[wife_name]
            setattr(main_obj, "wife", spouse_obj)

        husband_name = person.get("husband")
        if husband_name:
            main_obj = Person.people[person["name"]]
            spouse_obj = Person.people[husband_name]
            setattr(main_obj, "husband", spouse_obj)

    return instances
