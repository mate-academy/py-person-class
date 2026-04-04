class Person:
    people = {}

    def __init__(self,
                 name: str,
                 age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({name: self})


def create_person_list(people: list) -> list:
    person_list = []
    for person_dict in people:
        person_inst = Person(person_dict["name"], person_dict["age"])
        person_list.append(person_inst)

    for person_dict in people:
        if person_dict.get("wife"):
            if person_dict["wife"] != "None":
                person_inst.wife = Person.people[person_dict["wife"]]
                person_inst.wife.husband = Person.people[person_dict["name"]]
        if person_dict.get("husband"):
            if person_dict["husband"] != "None":
                person_inst.husband = Person.people[person_dict["husband"]]
                person_inst.husband.wife = Person.people[person_dict["name"]]
    return person_list
