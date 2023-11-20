class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    new_people_list = [Person(person["name"], person["age"])
                       for person in people_list]

    for person in people_list:
        if "husband" in person and person["husband"]:
            for woman in new_people_list:
                for man in new_people_list:
                    if woman.name == person["name"] and man.name == person["husband"]:
                        woman.husband = man
        elif "wife" in person and person["wife"]:
            for man in new_people_list:
                for woman in new_people_list:
                    if man.name == person["name"] and woman.name == person["wife"]:
                        man.wife = woman
    return new_people_list
