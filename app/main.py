class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_dict_list: list[dict]) -> list[Person]:
    person_list = []

    for person_dict in people_dict_list:
        name = person_dict["name"]
        age = person_dict["age"]
        person = Person(name, age)
        person_list.append(person)

    for person_dict in people_dict_list:
        name = person_dict["name"]
        wife_name = person_dict.get("wife")
        husband_name = person_dict.get("husband")

        person = Person.people[name]
        if wife_name:
            person.wife = Person.people[wife_name]
        if husband_name:
            person.husband = Person.people[husband_name]

    return person_list
