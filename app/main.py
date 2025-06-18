class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    instances = []
    for i in people:
        name = i["name"]
        age = i["age"]
        obj = Person(name, age)
        instances.append(obj)
    
    for i in people:
        obj = Person.people[i["name"]]
        if i.get("wife") is not None:
            obj.wife = Person.people[i["wife"]]
        if i.get("husband") is not None:
            obj.husband = Person.people[i["husband"]]
    
    return instances

