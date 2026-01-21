class Person:
    people = {}
    
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age
        self.wife: 'Person' = None
        self.husband: 'Person' = None
        Person.people[name] = self
    
    def __repr__(self) -> str:
        return f"Person(name='{self.name}', age={self.age})"

def create_person_list(people_list: list[dict]) -> list[Person]:
    person_instances: list[Person] = []
    
    # Create instances without relations
    for person_data in people_list:
        person_instances.append(Person(person_data["name"], person_data["age"]))
    
    # Establish relationships
    for person_data in people_list:
        person = Person.people[person_data["name"]]
        if "wife" in person_data and person_data["wife"]:
            person.wife = Person.people[person_data["wife"]]
        if "husband" in person_data and person_data["husband"]:
            person.husband = Person.people[person_data["husband"]]
    
    return person_instances
