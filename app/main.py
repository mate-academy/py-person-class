class Person:
    people = {}
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self

def create_person_list(people: list[dict]) -> list[Person]:
    Person_people = [Person(people_dict["name"], people_dict["age"]) for people_dict in people]
    for people_dict1 in people:
        if people_dict1.get("wife") != None:
            Person.people[people_dict1["name"]].wife = Person.people[people_dict1["wife"]]
        elif people_dict1.get("husband") != None:
            Person.people[people_dict1["name"]].husband = Person.people[people_dict1["husband"]]
        else:
            pass
    return Person_people
