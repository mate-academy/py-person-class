class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # self.wife = None
        # self.husband = None
        Person.people[name] = self


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
        elif character.__dict__.get("husband") is not None:
            character.husband = Person.people[character.__dict__.get("husband")]
    return character_list
