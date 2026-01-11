class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [
        Person(person_dict["name"],
        person_dict["age"])
        for person_dict in people
    ]
    for person_dict, person_obj in zip(people, result):
        wife_name = person_dict.get("wife")
        if wife_name != "":
            if Person.people.get(wife_name):
                person_obj.wife = Person.people[wife_name]
        husband_name = person_dict.get("husband")
        if husband_name != "":
            if Person.people.get(husband_name):
                person_obj.husband = Person.people[husband_name]
    return result



