class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    new_people_list = [Person(person_dict["name"], person_dict["age"])
                       for person_dict in people]

    for i in range(len(new_people_list)):
        if new_people_list[i].name == people[i]["name"]:
            if people[i].get("wife"):
                new_people_list[i].wife = Person.people[people[i]["wife"]]
            if people[i].get("husband"):
                new_people_list[i].husband \
                    = Person.people[people[i]["husband"]]
    return new_people_list
