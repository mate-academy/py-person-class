class Person:
    people = {}
    def __init__(self, name: str, age:int):
        self.name = name
        self.age = age
        Person.people[self.name] = self



def create_person_list(people: list) -> list:
    person_list = []
    for person_dict in people:
        person_obj = Person(person_dict["name"], person_dict["age"])
        person_list.append(person_obj)
    for person_dict in people:
        if "wife" in person_dict and person_dict["wife"]:
            Person.people[person_dict["name"]].wife = Person.people[person_dict["wife"]]
        if "husband" in person_dict and person_dict["husband"]:
            Person.people[person_dict["name"]].husband = Person.people[person_dict["husband"]]
    return person_list





