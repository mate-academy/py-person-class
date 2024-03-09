class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for human in people:
        first_hum = Person(human["name"], human["age"])
        if human.get("wife"):
            partner_type = "wife"
            other_part = "husband"
        else:
            partner_type = "husband"
            other_part = "wife"
        if human.get(partner_type):
            if human[partner_type] in Person.people:
                setattr(first_hum, partner_type,
                        Person.people[human[partner_type]])
                setattr(Person.people[human[partner_type]],
                        other_part, first_hum)
            else:
                setattr(first_hum, partner_type, human[partner_type])
    return [val for val in Person.people.values()]
    
