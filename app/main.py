class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    person_list = []

    for human in people:
        new_person = Person(name=human["name"], age=human["age"])
        if "wife" in human and human["wife"]:
            new_person.wife = human["wife"]
        if "husband" in human and human["husband"]:
            new_person.husband = human["husband"]

        Person.people.update({human["name"]: new_person})
        person_list.append(new_person)

    for _, person_instance in Person.people.items():
        if hasattr(person_instance, "wife") \
                and person_instance.wife in Person.people:

            person_instance.wife = [
                person_class for name, person_class in Person.people.items()
                if person_instance.wife == name
            ][0]
        if hasattr(person_instance, "husband") \
                and person_instance.husband in Person.people:

            person_instance.husband = [
                person_class for name, person_class in Person.people.items()
                if person_instance.husband == name
            ][0]

    return person_list
