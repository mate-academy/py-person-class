class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    dict_info_by_name = {}
    for current_person in people:
        Person(
            current_person["name"],
            current_person["age"]
        )
        dict_info_by_name[current_person["name"]] = current_person

    for person_cls_obj in Person.people.keys():
        if dict_info_by_name[person_cls_obj].get("wife") is not None:
            Person.people[person_cls_obj].wife = \
                Person.people[dict_info_by_name[person_cls_obj]["wife"]]
        elif dict_info_by_name[person_cls_obj].get("husband") is not None:
            Person.people[person_cls_obj].husband = \
                Person.people[dict_info_by_name[person_cls_obj]["husband"]]

    return list(Person.people.values())
