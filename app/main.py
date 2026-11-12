class Person:
    people = dict()
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        # self.wife = None
        # self.husband = None
        Person.people[name] = self

# Person.__dict__

def create_person_list(people: list) -> list:
    character_list = []
    for person in people:
        if "wife" in person and person["wife"] is not None:
            character = Person(name=person["name"], age=person["age"])
            character.wife = person["wife"]
        elif "husband" in person and person["husband"] is not None:
            character = Person(name=person["name"], age=person["age"])
            character.husband = person["husband"]
        else:
            character = Person(name=person["name"], age=person["age"])
        character_list.append(character)
    for character in character_list:
        if character.__dict__.get("wife") is not None:
            character.wife = Person.people[character.__dict__.get("wife")]
            #print(character.name, character.age, character.wife, type(character.wife), character.wife.name)
        elif character.__dict__.get("husband") is not None:
            character.husband = Person.people[character.__dict__.get("husband")]
            #print(character.name, character.age, character.husband, type(character.husband), character.husband.name)
    return character_list