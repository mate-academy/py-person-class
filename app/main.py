class Person:
    
    people = {}
    
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people):
    person_dict = {}
    for person_info in people:
        person = Person(person_info["name"], person_info["age"])
        person_dict[person.name] = person 
    
    for person_info in people:
        person = person_dict[person_info["name"]]
        if person_info.get("wife"):
            person.wife = person_dict.get(person_info["wife"])
        if person_info.get("husband"):
            person.husband = person_dict.get(person_info["husband"])
    
    return list(person_dict.values())
