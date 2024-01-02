class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
#        self.wife = None
#        self.husband = None
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)

        if person_data.get("wife"):
            if person_data["wife"] == None:
                continue
            else:    
                wife_name = person_data["wife"]
                if wife_name in Person.people:
                    Person.wife = Person.people[wife_name]

        if person_data.get("husband"):
            husband_name = person_data["husband"]
            if husband_name in Person.people:
                Person.husband = Person.people[husband_name]
        
#        if person.wife is None:
#            person_list.append(person = Person(name, age))

        person_list.append(person)
    return person_list
