class Person:
    people = {}

    def __init__(self, name: str, age: str) -> str:
        self.name = name
        self.age = age
        Person.people[name] = self

    def __repr__(self: str) -> str:
        spouse_name = (
            getattr(self, "wife", None)
            or getattr(self, "husband", None)
        )
        spouse_name = spouse_name.name if spouse_name else None
        spouse_type = "wife" if hasattr(self, "wife") else "husband"
        return (
            f"Person(name={self.name}, age={self.age}"
            + (f", {spouse_type}={spouse_name}"
               if spouse_name else "") + ")"
        )


def create_person_list(people_list: list) -> list:
    person_instances = []

    # First, create Person instances without assigning spouses
    for person_dict in people_list:
        (
            person_instances.append(
                Person(person_dict["name"], person_dict["age"]))
        )
    # Now, assign spouses to the Person instances
    for person_dict, person_instance in zip(
            people_list, person_instances):
        if person_dict.get("wife"):
            setattr(
                person_instance, "wife",
                Person.people[person_dict["wife"]]
            )
        elif person_dict.get("husband"):
            setattr(
                person_instance, "husband",
                Person.people[person_dict["husband"]]
            )

    return person_instances
