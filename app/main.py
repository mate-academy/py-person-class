class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    Person.people.clear()
    persons = [
        Person(person_dict["name"], person_dict["age"])
        for person_dict in people_list
    ]

    for people_ls, person_dict in zip(people_list, persons):
        wife_name = people_ls.get("wife")
        if wife_name is not None:
            person_dict.wife = Person.people[wife_name]
        husband_name = people_ls.get("husband")
        if husband_name is not None:
            person_dict.husband = Person.people[husband_name]
    return persons
