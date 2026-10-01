class Person:
    # Class attribute to store instances by their name
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        # Add the new instance to the people dictionary
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    # Optional: clear previous entries if the function is called multiple times
    Person.people.clear()
    
    person_instances = []

    # First pass: create all Person instances and store them
    for person_dict in people_data:
        person = Person(name=person_dict["name"], age=person_dict["age"])
        person_instances.append(person)

    # Second pass: link spouses (wife/husband) if applicable
    for person_dict in people_data:
        person = Person.people[person_dict["name"]]
        
        if "wife" in person_dict and person_dict["wife"] is not None:
            person.wife = Person.people[person_dict["wife"]]
        elif "husband" in person_dict and person_dict["husband"] is not None:
            person.husband = Person.people[person_dict["husband"]]

    return person_instances
