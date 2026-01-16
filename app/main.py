class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()

    created_list = [Person(d["name"], d["age"]) for d in people]

    for inst, person_dict in zip(created_list, people):
        if (wife_name := person_dict.get("wife")) and \
           (wife_obj := Person.people.get(wife_name)):
            inst.wife = wife_obj

        if (husband_name := person_dict.get("husband")) and \
           (husband_obj := Person.people.get(husband_name)):
            inst.husband = husband_obj

    return created_list
