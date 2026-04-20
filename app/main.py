class Person:
    pass


def create_person_list(people: list[dict]) -> list[Person]:
    # reset storage in case function is called multiple times
    Person.people = {}

    person_list = []

    # 1️⃣ create all Person instances
    for p in people:
        person = Person(p["name"], p["age"])
        person_list.append(person)

    # 2️⃣ link wife / husband
    for p in people:
        person = Person.people[p["name"]]

        # link wife
        if "wife" in p and p["wife"] is not None:
            spouse = Person.people[p["wife"]]
            person.wife = spouse
            # ensure reverse link exists
            if not hasattr(spouse, "husband"):
                spouse.husband = person

        # link husband
        if "husband" in p and p["husband"] is not None:
            spouse = Person.people[p["husband"]]
            person.husband = spouse
            # ensure reverse link exists
            if not hasattr(spouse, "wife"):
                spouse.wife = person

    return person_list