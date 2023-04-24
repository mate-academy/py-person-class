class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people_dict: list) -> list:
    person_list = []
    for p_dict in people_dict:
        p = Person(p_dict["name"], p_dict["age"])
        person_list.append(p)
    for p_dict in people_dict:
        if "husband" in p_dict and p_dict["husband"] is not None:
            Person.people[p_dict["name"]].husband = \
                Person.people[p_dict["husband"]]
        elif "wife" in p_dict and p_dict["wife"] is not None:
            Person.people[p_dict["name"]].wife = Person.people[p_dict["wife"]]
    return person_list
