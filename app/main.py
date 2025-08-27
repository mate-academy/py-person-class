class Person:
    people = {}
    def __init__(self, name: str, age:int):
        self.name = name
        self.age = age
        Person.people[self.name] = self



def create_person_list(people: list) -> list:
    Person.people.clear()
    person_list = [Person(person_dict["name"], person_dict["age"]) for person_dict in people]
    for person_dict in people:
        wife_name = person_dict.get("wife")
        husband_name = person_dict.get("husband")
        if wife_name:
            Person.people[person_dict["name"]].wife = Person.people[wife_name]
        if husband_name:
            Person.people[person_dict["name"]].husband = Person.people[husband_name]
    return person_list



