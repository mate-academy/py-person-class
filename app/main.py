class Person:
    # Dicionário para armazenar instâncias por nome
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def set_spouse(self, spouse: "Person", relationship: str) -> None:
        if (spouse and relationship in ("wife", "husband") and
            ((relationship == "wife" and not getattr(self, "wife", None) and
              not getattr(spouse, "husband", None)) or
             (relationship == "husband" and not getattr(self, "husband", None) and
              not getattr(spouse, "wife", None)))):
            if relationship == "wife":
                self.wife = spouse
                spouse.husband = self
            else:
                self.husband = spouse
                spouse.wife = self


def create_person_list(people: list[dict[str, str | int]]) -> list[Person]:
    person_objects = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for person in people:
        person_instance = Person.people.get(person["name"])

        if (wife_name := person.get("wife")) and (
                wife := Person.people.get(wife_name)):
            person_instance.set_spouse(wife, "wife")

        if (husband_name := person.get("husband")) and (
                husband := Person.people.get(husband_name)):
            person_instance.set_spouse(husband, "husband")

    return person_objects

