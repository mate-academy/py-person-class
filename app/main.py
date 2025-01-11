class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for i, person_info in enumerate(people):
        spouse_name = person_info.get("wife") or person_info.get("husband")
        if spouse_name:
            spouse = Person.people.get(spouse_name)
            if person_info.get("wife"):
                person_list[i].wife = spouse
                if spouse:
                    spouse.husband = person_list[i]
            elif person_info.get("husband"):
                person_list[i].husband = spouse
                if spouse:
                    spouse.wife = person_list[i]

    return person_list
