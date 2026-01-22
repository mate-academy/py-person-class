class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list):
    # Step 1: Create Person instances using list comprehension
    person_list = [Person(p["name"], p["age"]) for p in people_data]

    # Step 2: Assign relationships using short-circuit logic
    for p in people_data:
        person = Person.people[p["name"]]
        p.get("wife") and setattr(person, "wife", Person.people[p["wife"]])
        p.get("husband") and setattr(person, "husband", Person.people[p["husband"]])

    return person_list
