class Person:
    people = {}

    def __init__(self,
                 name: str,
                 age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({name: self})


def create_person_list(people: list) -> list:
    person_list = [Person(person_dict["name"], person_dict["age"])
                   for person_dict in people]

    for person_dict in people:
        this_inst = Person.people[person_dict["name"]]
        if person_dict.get("wife"):
            this_inst.wife = Person.people[person_dict["wife"]]
            this_inst.wife.husband = Person.people[person_dict["name"]]
        if person_dict.get("husband"):
            this_inst.husband = Person.people[person_dict["husband"]]
            this_inst.husband.wife = Person.people[person_dict["name"]]
    return person_list
