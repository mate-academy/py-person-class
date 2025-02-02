class Person:
    people = {}
    
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.spouse = None
        Person.people[name] = self

def create_person_list(people_list) -> list:
    person_instances = []
    
    for person_data in people_list:
        person_instances.append(Person(person_data['name'], person_data['age']))
    
    for person_data in people_list:
        person_instance = Person.people[person_data['name']]
        spouse_key = 'wife' if 'wife' in person_data else 'husband'
        spouse_name = person_data.get(spouse_key)
        
        if spouse_name and spouse_name in Person.people:
            setattr(person_instance, spouse_key, Person.people[spouse_name])
    
    return person_instances