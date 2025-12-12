from typing import List, Dict, Any, Optional, Tuple


class Person:
    """
    A class representing a person. It stores all created instances
    in a class attribute called 'people'.
    """
    # Class Attribute: Dictionary to store all Person instances by name.
    # Key: name (str), Value: Person object reference
    people: Dict[str, 'Person'] = {}

    def __init__(self, name: str, age: int):
        """
        Constructor that initializes name and age, and adds the instance to Person.people.
        """
        self.name: str = name
        self.age: int = age

        # Add the current instance to the class dictionary
        Person.people[name] = self

    def __repr__(self) -> str:
        """Helper method for convenient object representation."""
        # Dynamically check for the partner attribute ('wife' or 'husband')
        partner_obj = getattr(self, 'wife', None) or getattr(self, 'husband', None)
        partner_name = partner_obj.name if partner_obj else "None"
        return f"Person(name='{self.name}', age={self.age}, partner='{partner_name}')"


def create_person_list(people_dicts: List[Dict[str, Any]]) -> List[Person]:
    """
    Converts a list of dictionaries into a list of Person instances and
    establishes partner links between them.

    :param people_dicts: List of dictionaries with person data.
    :return: List of Person instances.
    """

    # 1. Clear the class attribute before starting, ensuring a clean slate for new data
    Person.people = {}
    person_instances: List[Person] = []

    # --- Stage 1: Create all instances (Populates Person.people) ---
    for person_data in people_dicts:
        instance = Person(name=person_data['name'], age=person_data['age'])
        person_instances.append(instance)

    # --- Stage 2: Establish the relationships (Requires all objects to be in the cache) ---
    #
    for person_data in people_dicts:
        name = person_data['name']
        instance = Person.people[name]  # Retrieve the instance created in Stage 1

        partner_name: Optional[str] = None
        partner_attr: Optional[str] = None  # 'wife' or 'husband' attribute name

        # Check for 'wife' attribute
        if 'wife' in person_data and person_data['wife'] is not None:
            partner_name = person_data['wife']
            partner_attr = 'wife'
        # Check for 'husband' attribute
        elif 'husband' in person_data and person_data['husband'] is not None:
            partner_name = person_data['husband']
            partner_attr = 'husband'

        if partner_name and partner_attr:
            # Get the partner object from the class cache (Person.people)
            partner_instance = Person.people.get(partner_name)

            if partner_instance:
                # Dynamically set the attribute ('wife' or 'husband') on the instance,
                # linking it to the partner's object.
                setattr(instance, partner_attr, partner_instance)

    return person_instances


# --- Example Usage ---
people_data = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]

person_list = create_person_list(people_data)

print("--- Verification of Objects and Attributes ---")
ross = person_list[0]
rachel = person_list[2]

print(f"1. Ross: {ross}")
print(f"   Ross's wife name: {ross.wife.name == 'Rachel'}")
print(f"   Ross's wife is Rachel's object: {ross.wife is rachel}")  # True

print(f"\n3. Rachel: {rachel}")
print(f"   Rachel's husband name: {rachel.husband.name == 'Ross'}")
print(f"   Rachel's husband is Ross's object: {rachel.husband is ross}")  # True
print(f"   Rachel's husband's wife is Rachel: {rachel.husband.wife is rachel}")  # True

print("\n--- Verification of Person.people Class Attribute ---")
print(f"Person.people size: {len(Person.people)}")
print(f"Person.people['Ross'] is Ross's object: {Person.people['Ross'] is ross}")