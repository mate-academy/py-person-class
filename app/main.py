class Person:
    # write your code here
    people = []
    
    def __init__(self, name: str, age: int) -> None:
        
        self.name = name
        self.age = age
        self.spouse = None
        Person.people.append(self)

def create_person_list(people: list) -> list:
    # write your code here
    for person in people:
        name = person['name']
        age = person['age']
        Person(name, age)

        person_instance = Person.people[person_data['name']]
        spouse_key = 'wife' if 'wife' in person_data else 'husband'
        spouse_name = person_data.get(spouse_key)
        
        if spouse_name and spouse_name in Person.person:
            setattr(person_instance, spouse_key, Person.person[spouse_name])
    
    
    return Person.people