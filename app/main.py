class Person:
    people = {}
    # dictionary for saving links to class objects

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    dict_info_by_name = {}
    # dictionary for saving full people information: name, age, marriage
    for person in people:
        dict_info_by_name[person["name"]] = person
        Person(
            person["name"],
            person["age"]
        )

    for person_name in Person.people.keys():
        if dict_info_by_name[person_name].get("wife") is not None:
            Person.people[person_name].wife = \
                Person.people[dict_info_by_name[person_name]["wife"]]
        elif dict_info_by_name[person_name].get("husband") is not None:
            Person.people[person_name].husband = \
                Person.people[dict_info_by_name[person_name]["husband"]]

    return list(Person.people.values())
