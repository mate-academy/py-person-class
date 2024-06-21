class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"


def create_person_list(people: list) -> list:
    for one_person in people:
        Person(one_person["name"], one_person["age"])
    for one_person in people:
        person_instance = Person.people[one_person["name"]]
        spouse_name = one_person.get("wife") or one_person.get("husband")
        spouse_instance = Person.people.get(spouse_name)
        if "wife" in one_person:
            if one_person["wife"] is not None:
                person_instance.wife = spouse_instance
        elif "husband" in one_person:
            person_instance.husband = spouse_instance
    return list(Person.people.values())
