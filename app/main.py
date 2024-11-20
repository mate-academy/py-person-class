from typing import List, Dict, Any


class Person:
    people: Dict[str, "Person"] = (
        {}
    )  # Stores all Person instances by their names

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # Add the instance to the `people` dictionary
        Person.people[name] = self

    @staticmethod
    def create_person_list(people: List[Dict[str, Any]]) -> List["Person"]:
        """
        Create a list of Person instances from a list of dictionaries.

        Args:
            people: A list of dictionaries, each representing a person.

        Returns:
            A list of Person instances with relationships established.
        """
        person_list = []
        for person_data in people:
            person_list.append(
                Person(name=person_data["name"], age=person_data["age"])
            )

        for person_data in people:
            person_instance = Person.people[person_data["name"]]
            spouse_key = "wife" if "wife" in person_data else "husband"
            if person_data.get(spouse_key):
                setattr(
                    person_instance,
                    spouse_key,
                    Person.people[person_data[spouse_key]],
                )

        return person_list


# Example usage with the provided input
people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"},
]

person_list = Person.create_person_list(people)

# Test cases
assert isinstance(person_list[0], Person)  # True
assert person_list[0].name == "Ross"
assert person_list[0].wife is person_list[2]  # True
assert person_list[0].wife.name == "Rachel"

assert person_list[1].name == "Joey"
try:
    assert person_list[1].wife  # Joey does not have a wife
except AttributeError:
    pass

assert isinstance(person_list[2], Person)  # True
assert person_list[2].name == "Rachel"
assert person_list[2].husband is person_list[0]  # True
assert person_list[2].husband.name == "Ross"
assert person_list[2].husband.wife is person_list[2]  # True

assert Person.people == {
    "Ross": person_list[0],
    "Joey": person_list[1],
    "Rachel": person_list[2],
}
