class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None

        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        name = person["name"]
        age = person["age"]
        Person(name, age)  
        
    for person in people:
        current_instance = Person.people[person["name"]]

        if person.get("wife"):
            current_instance.wife = Person.people[person["wife"]]
        
        if person.get("husband"):
            current_instance.husband = Person.people[person["husband"]]

    return list(Person.people.values())
