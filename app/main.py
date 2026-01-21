class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    instances = [Person(pd["name"], pd["age"]) for pd in people]
    for pd in people:
        ppl = Person.people[pd["name"]]
        spouse_name = pd.get("wife") or pd.get("husband")
        attr = None
        if pd.get("wife"):
            attr = "wife"
        elif pd.get("husband"):
            attr = "husband"
        if attr and spouse_name:
            setattr(ppl, attr, Person.people.get(spouse_name))
    return instances
