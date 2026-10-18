class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    for person_dict in people_data:
        if person_dict["name"] not in Person.people:
            Person(person_dict["name"], person_dict["age"])

    for person_dict in people_data:
        current_person = Person.people[person_dict["name"]]
        
        if "wife" in person_dict and person_dict["wife"] is not None:
            current_person.wife = Person.people[person_dict["wife"]]
            
        if "husband" in person_dict and person_dict["husband"] is not None:
            current_person.husband = Person.people[person_dict["husband"]]

    return [Person.people[person_dict["name"]] for person_dict in people_data]
