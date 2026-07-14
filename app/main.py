class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        Person.people[name] = self
        self.age = age
        self.name = name


def create_person_list(people_data: list) -> list:
    result = []
    for person_dict in people_data:
        person = Person(person_dict["name"], person_dict["age"])
        result.append(person)

    for person_dict in people_data:
        person = Person.people[person_dict["name"]]
        wife_name = person_dict.get("wife")
        if wife_name:
            person.wife = Person.people[wife_name]
        husband_name = person_dict.get("husband")
        if husband_name:
            person.husband = Person.people[husband_name]
    return result
