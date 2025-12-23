class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        """
        It represents a person and manages a centralized registry of instances.

        Class attributes:
            people (dict): Dictionary that stores all created instances,
            using the name as the key and the Person object as the value.

        Class method:
            Initializes a new instance of Person and registers
            it 8n the class dictionary.
        """
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    """
    Convert dictionaries into Person instances and link their relationships.

    Create the objects in the first pass and in the second pass
    establish the "wife" / "husband" attributes, connecting them to each other.
    """
    for ppl in people:
        Person(ppl.get("name"), ppl.get("age"))
    for ppl in people:
        name = ppl.get("name")
        individual = Person.people.get(name)
        for relation in ppl:
            if relation in ["wife", "husband"] and ppl.get(relation) is not None:
                partner_name = ppl.get(relation)
                partner_instance = Person.people.get(partner_name)
                setattr(individual, relation, partner_instance)
    return [Person.people.get(ppl.get("name")) for ppl in people]
