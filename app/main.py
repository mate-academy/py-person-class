class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        # Add each new Person instance to the class dictionary
        Person.people[self.name] = self


def create_person_list(people_data: list) -> list:
    person_list = []
    
    # First pass: create all Person instances and populate the list
    for person_dict in people_data:
        name = person_dict["name"]
        age = person_dict["age"]
        person = Person(name, age)
        person_list.append(person)
        
    # Second pass: assign wife/husband attributes using the Person.people registry
    for person_dict, person_instance in zip(people_data, person_list):
        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            person_instance.wife = Person.people[wife_name]
        elif "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            person_instance.husband = Person.people[husband_name]
            
    return person_list
