class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list:
    person_list = [Person(each["name"], each["age"]) for each in people]
    for each in people:
        person_instance = Person.people[each["name"]]
        if "wife" in each and each["wife"] is not None:
            if each["wife"] in Person.people:
                person_instance.wife = Person.people[each["wife"]]
            else:
                print(f"Warning: Wife {each["wife"]} for {each["name"]} "
                      f"not found.")
        if "husband" in each and each["husband"] is not None:
            if each["husband"] in Person.people:
                person_instance.husband = Person.people[each["husband"]]
            else:
                print(f"Warning: Husband {each["husband"]} for {each["name"]} "
                      f"not found.")

    return person_list
