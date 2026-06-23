class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age  
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_instances = []
    
    for p in people:
        person = Person(p["name"], p["age"])
        person_instances.append(person)
        
    for p_dict, person in zip(people, person_instances):
        if p_dict.get("wife") is not None:
            person.wife = Person.people[p_dict["wife"]]
            
        if p_dict.get("husband") is not None:
            person.husband = Person.people[p_dict["husband"]]
            
    return person_instances
