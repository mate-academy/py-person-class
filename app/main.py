class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"


def create_person_list(people_data: list) -> list:

    people_instances = []

    for person in people_data:
        instance = person["name"], person["age"]
        people_instances.append(instance)

    for person in people_data:
        instance = Person.people[person["name"]]
        for i in Person.people:
            if "wife" in i and i["wife"] is not None:
                Person.people[i["name"]].wife = Person.people[i["wife"]]

            if "husband" in i and i["husband"] is not None:
                Person.people[i["name"]].husband = Person.people[i["husband"]]

        spouse_key = "wife" if "wife" in person else "husband"
        spouse_name = person.get(spouse_key)

        if spouse_name:
            setattr(instance, spouse_key, person.get(spouse_name))

    return people_instances
