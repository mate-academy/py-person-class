class Person:
    dict_of_person_obj = []
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.dict_of_person_obj[self.name] = self

def create_dict_of_person_obj(people: list) -> list:
    list_person = []
    for person in people:
        list_person.append(Person(person.get("name"),person.get("age")))
        if not isinstance(person.get('wife'), None):
             person["wife"] = Person.dict_of_person_obj.get(person["name"])
        if not isinstance(person.get('husband'), None):
             person["husband"] = Person.dict_of_person_obj.get(person["name"])
    return list_person
