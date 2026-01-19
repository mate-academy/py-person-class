class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(p["name"], p["age"]) for p in people]
    
    for i, person_dict in enumerate(people):
        person_instance = people_list[i]
        
        wife_name = person_dict.get("wife")
        if wife_name is not None:
            person_instance.wife = Person.people.get(wife_name)

        husband_name = person_dict.get("husband")
        if husband_name is not None:
            person_instance.husband = Person.people.get(husband_name)

    return people_list
