class Person:
    people = {}
    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
        created = [Person(d["name"], d["age"]) for d in people]
        for element,inst in zip(people,created):
            if element.get("wife") is not None:
                inst.wife = Person.people[element["wife"]]
            if element.get("husband") is not None:
                inst.husband = Person.people[element["husband"]]
        return created





