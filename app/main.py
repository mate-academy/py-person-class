from typing import List, Dict, Optional


class Person:
    people: Dict[str, "Person"] = {}
    # Class attribute to store instances by name

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        self.wife: Optional["Person"] = None
        self.husband: Optional["Person"] = None
        Person.people[name] = self  # Store instance in the class attribute

    @classmethod
    def create_person_list(cls, people_list: List[Dict[str, any]]) \
            -> List["Person"]:
        # First, create all Person instances
        person_instances = [cls(person["name"], person["age"])
                            for person in people_list]

        # Second, link spouses
        for person_dict in people_list:
            person = cls.people.get(person_dict["name"])
            if person:
                if "wife" in person_dict and person_dict["wife"]:
                    person.wife = cls.people.get(person_dict["wife"])
                if "husband" in person_dict and person_dict["husband"]:
                    person.husband = cls.people.get(person_dict["husband"])

        return person_instances


if __name__ == "__main__":
    # Example Usage
    data = [
        {"name": "Ross", "age": 30, "wife": "Rachel"},
        {"name": "Joey", "age": 29, "wife": None},
        {"name": "Rachel", "age": 28, "husband": "Ross"}
    ]

    person_list = Person.create_person_list(data)

    # Tests
    print(isinstance(person_list[0], Person))  # True
    print(person_list[0].name == "Ross")  # True
    print(person_list[0].wife is person_list[2])  # True
    print(person_list[0].wife.name == "Rachel")  # True
    print(person_list[1].name == "Joey")  # True
    print(hasattr(person_list[1], "wife"))  # False
    print(isinstance(person_list[2], Person))  # True
    print(person_list[2].name == "Rachel")  # True
    print(person_list[2].husband is person_list[0])  # True
    print(person_list[2].husband.name == "Ross")  # True
    print(person_list[2].husband.wife is person_list[2])  # True

    # Check class attribute
    print(Person.people)
