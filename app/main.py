class Person:
    people = {}

    def __init__(
            self,
            name: str,
            age: int
    ) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_persons = []
    for human in people:
       person_item = Person(human["name"], human["age"])
       list_of_persons.append(person_item)
    for human_first_instance in list_of_persons:
        human_dict_element = None
        for human_dict in people:
            if human_first_instance.name == human_dict["name"]:
                human_dict_element = human_dict
                break
        if "wife" in human_dict_element and human_dict_element["wife"] != None:
            human_first_instance.wife = Person.people[human_dict_element["wife"]]
        elif "husband" in human_dict_element and human_dict_element["husband"] != None:
            human_first_instance.husband = Person.people[human_dict_element["husband"]]
    return list_of_persons
