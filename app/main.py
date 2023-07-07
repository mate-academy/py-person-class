class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        self.people[name] = self

    def create_person_list(people: list) -> list:
        persons = []
        for person in people:
            name = person["name"]
            age = person["age"]
            new_person = Person(name, age)
            spouse_name = person.get("wife") or person.get("husband")
            if spouse_name:
                if spouse_name in Person.people:
                    spouse = Person.people[spouse_name]
                    if "wife" in person:
                        new_person.wife = spouse
                    else:
                        new_person.husband = spouse
            persons.append(new_person)
        return persons
