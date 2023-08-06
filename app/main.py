class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.add_object(self)

    @classmethod
    def add_object(cls, obj: object) -> None:
        cls.people[obj.name] = obj


def create_person_list(people: list[dict]) -> list[Person]:
    result = []

    for pers in people:
        person = Person(name=pers["name"], age=pers["age"])
        result.append(person)

    for pers in people:
        person = Person.people[pers["name"]]
        if "wife" in pers and pers["wife"] is not None:
            wife_name = pers["wife"]
            wife = Person.people.get(wife_name)
            if wife:
                person.wife = wife
                wife.husband = person
        elif "husband" in pers and pers["husband"] is not None:
            husband_name = pers["husband"]
            husband = Person.people.get(husband_name)
            if husband:
                person.husband = husband
                husband.wife = person

    return result
