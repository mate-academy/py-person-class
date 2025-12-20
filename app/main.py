class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        spouse = None
        if "wife" in person or "husband" in person:
            spouse = person["wife"] if "wife" in person else person["husband"]
            spouse_key = "wife" if "wife" in person else "husband"
        if spouse:
            spouse_info = next(
                (partner for partner in people if partner["name"] == spouse),
                None)
            if spouse_key == "wife":
                new_person.wife = Person(
                    spouse_info["name"],
                    spouse_info["age"])
                new_person.wife.husband = new_person
            else:
                new_person.husband = Person(spouse_info["name"],
                                            spouse_info["age"])
                new_person.husband.wife = new_person
        person_list.append(new_person)
    return person_list
