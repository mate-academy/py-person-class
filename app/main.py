class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_people = [Person(inf_dict.get("name"), inf_dict.get("age"))
                      for inf_dict in people]
    for info in people:
        key_name = Person.people.get(info.get("name"))
        if info.get("wife") is not None:
            key_name.wife = Person.people.get(info.get("wife"))
        if info.get("husband") is not None:
            key_name.husband = Person.people.get(info.get("husband"))
    return list_of_people
