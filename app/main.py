class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    new_people_list = []
    for person in people_list:
        new_people_list.append(Person(person["name"], person["age"]))
    for person in people_list:
        if "husband" in person and person["husband"]:
            for woman in new_people_list:
                if woman.name == person["name"]:
                    for man in new_people_list:
                        if man.name == person["husband"]:
                            woman.husband = man
        if "wife" in person and person["wife"]:
            for man in new_people_list:
                if man.name == person["name"]:
                    for woman in new_people_list:
                        if woman.name == person["wife"]:
                            man.wife = woman
    return new_people_list
