class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    person_list = []
    for person_dict in people_data:
        person = Person(person_dict["name"], person_dict["age"])
        person_list.append(person)

    for person_dict in people_data:
        current_person = Person.people[person_dict["name"]]

        wife_name = person_dict.get("wife")
        husband_name = person_dict.get("husband")

        if wife_name:
            current_person.wife = Person.people[wife_name]
            current_person.wife.husband = current_person

        if husband_name:
            current_person.husband = Person.people[husband_name]
            current_person.husband.wife = current_person

    return person_list
