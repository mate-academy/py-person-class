from typing import List, Dict, Optional


class Person:
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        self.wife: Optional[str] = None
        self.husband: Optional[str] = None
        Person.people[self.name] = self


def create_person_list(people: List[Dict[str, str]]) -> List[Person]:
    lista_of_people: List[Person] = []
    for person in people:
        obj_person = Person(person["name"], int(person["age"]))
        lista_of_people.append(obj_person)

        if person.get("wife"):
            obj_person.wife = person["wife"]
        else:
            obj_person.husband = person["husband"]

    for index, person_obj in enumerate(lista_of_people):
        if person_obj.wife and person_obj.wife in Person.people:
            person_obj.wife = Person.people[person_obj.wife]
        if person_obj.husband and person_obj.husband in Person.people:
            person_obj.husband = Person.people[person_obj.husband]

    return lista_of_people
