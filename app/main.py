class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(name=people_dict["name"], age=people_dict["age"])
                   for people_dict in people]

    for people_dict in people:
        person = Person.people[people_dict["name"]]
        wife_name = people_dict.get("wife")
        if wife_name:
            person.wife = Person.people[wife_name]

        husband_name = people_dict.get("husband")
        if husband_name:
            person.husband = Person.people[husband_name]

    return people_list
