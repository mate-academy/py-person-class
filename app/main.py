class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def __repr__(self) -> str:
        return f"Person({self.name}, {self.age})"


def create_person_list(people: list) -> list:

    [Person(person_info["name"], person_info["age"]) for person_info in people]

    for person_info in people:
        person = Person.people[person_info["name"]]
        spouse_name = person_info.get("wife") or person_info.get("husband")
        if spouse_name:
            spouse = Person.people.get(spouse_name)
            if spouse:
                if "wife" in person_info:
                    setattr(person, "wife", spouse)
                elif "husband" in person_info:
                    setattr(person, "husband", spouse)

    return list(Person.people.values())
