class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_dict in people:
        person_list.append(Person
                           (person_dict["name"], person_dict["age"]))

    for i in range(len(person_list)):
        person = person_list[i]
        person_dict = people[i]
        spouse = person_dict.get("wife") or person_dict.get("husband")
        if spouse is not None:
            spouse_person = Person.people[spouse]
            if "wife" in person_dict:
                person.wife = spouse_person
            else:
                person.husband = spouse_person
    return person_list
