from typing import Dict, List, Optional, Any


class Person:
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife: Optional["Person"] = None
        self.husband: Optional["Person"] = None
        Person.people[name] = self


def create_person_list(people_data: List[Dict[str, Any]]) -> List[Person]:
    person_list = []
    
    for data in people_data:
        person = Person(data["name"], data["age"])
        person_list.append(person)
        
    for data in people_data:
        person = Person.people[data["name"]]
        
        wife_name = data.get("wife")
        if wife_name is not None:
            person.wife = Person.people[wife_name]
            
        husband_name = data.get("husband")
        if husband_name is not None:
            person.husband = Person.people[husband_name]
            
    return person_list
