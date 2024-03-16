class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_data in people:
        person_list.append(Person(person_data["name"], person_data["age"]))
    for person_data in people:
        for person_dict in person_list:
            if person_dict.name == person_data["name"]:
                if person_data.get("husband"):
                    husband_name = person_data["husband"]
                    for person_dict_2 in person_list:
                        if person_dict_2.name == husband_name:
                            person_dict.husband = person_dict_2
                if person_data.get("wife"):
                    wife_name = person_data["wife"]
                    for person_dict_2 in person_list:
                        if person_dict_2.name == wife_name:
                            person_dict.wife = person_dict_2
    return person_list
