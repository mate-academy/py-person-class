class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for character in people:
        person = Person(character["name"], character["age"])
        person_list.append(person)

    for character in people:
        name = character["name"]
        name_of_character = character.get("wife") or character.get("husband")

        if name_of_character:
            married = Person.people.get(name_of_character)
            if married:
                if (name_of_character in Person.people and
                        "wife" in Person.people[name_of_character].__dict__):
                    Person.people[name].husband = married
                else:
                    Person.people[name].wife = married

    return person_list
