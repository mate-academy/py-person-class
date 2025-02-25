class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, " \
               f"{"wife=" + self.wife.name if hasattr(self, "wife") else "wife=None"}, " \
               f"{"husband=" + self.husband.name if hasattr(self, "husband") else "husband=None"})"


def create_person_list(people_list):

    person_instances = [Person(person["name"], person["age"]) for person in people_list]

    for person in people_list:
        person_instance = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            person_instance.wife = Person.people.get(person["wife"])
        elif "husband" in person and person["husband"]:
            person_instance.husband = Person.people.get(person["husband"])

    return person_instances