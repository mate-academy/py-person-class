class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.people[self.name, self.age] = self


def create_person_list(people_dict: list) -> list:
    person_list = []
    for p_dict in people_dict:
        p = Person(p_dict["name"], p_dict["age"])
        p_dict["ss"] = p
        person_list.append(p)
    for p_dict in people_dict:
        if "husband" in p_dict:
            if p_dict["husband"] is not None:
                for i in range(len(person_list)):
                    if p_dict["husband"] in person_list[i].name:
                        person_list[i].wife = p_dict["ss"]
                        break
        elif "wife" in p_dict:
            if p_dict["wife"] is not None:
                for i in range(len(person_list)):
                    if p_dict["wife"] in person_list[i].name:
                        person_list[i].husband = p_dict["ss"]
                        break
        else:
            pass
    return person_list
