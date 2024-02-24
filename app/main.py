class Person:
    people = {}

    def __init__(self, name: str, age: int, wife: str | None = None,
                 husband: str | None = None) -> None:
        self.name = name
        self.age = age
        self.wife = wife
        self.husband = husband
        self.people[name] = self

    def create_person_list(self, people: list) -> list:
        person_list = []
        for person in people:
            name = person["name"]
            age = person["age"]
            spouse = person.get("wife") or person.get("husband")
            spouse_person = self.people.get(spouse)
            if not spouse_person:
                spouse_person = Person(spouse, None)
            if person["wife"]:
                person_list.append(Person(name, age, wife=spouse_person))
            elif person["husband"]:
                person_list.append(Person(name, age, husband=spouse_person))
            else:
                person_list.append(Person(name, age))
        return person_list
