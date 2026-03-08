class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self

def create_person_list(people_dicts: list) -> list:
    [Person(p.get("name"), p.get("age")) for p in people_dicts]

    person_instances = []
    for p_dict in people_dicts:
        person = Person.people.get(p_dict.get("name"))
        
        wife_name = p_dict.get("wife")
        husband_name = p_dict.get("husband")

        if wife_name:
            person.wife = Person.people.get(wife_name)
        if husband_name:
            person.husband = Person.people.get(husband_name)
            
        person_instances.append(person)
        
    return person_instances
