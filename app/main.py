class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def is_married(self) -> bool:
        second_half = None
        if hasattr(self, "wife"):
            second_half = self.wife
        elif hasattr(self, "husband"):
            second_half = self.husband
        return second_half is not None

    def wedding(
        self,
        person: "Person",
    ) -> None | ValueError:
        if person.is_married():
            raise ValueError(f"{person.name} is married")
        if self.is_married():
            raise ValueError(f"{self.name} is married")
        self.wife = person
        person.husband = self
        print(f"{self.name} married {person.name}")


def create_person_list(people: list[dict]) -> list[Person]:
    people_list = []
    for human_dict in people:
        name = human_dict.get("name")
        age = human_dict.get("age")

        person = Person(name, age)
        people_list.append(person)
    for person in people:
        name = person.get("name")
        wife = person.get("wife")
        husband = person.get("husband")
        if wife or husband:
            if wife:
                Person.people.get(name).wife = Person.people.get(wife)
            else:
                Person.people.get(name).husband = Person.people.get(husband)
    return people_list


def get_married_couples(person_list: list[Person]) -> list[tuple]:
    seen = set()
    for person in person_list:
        second_half = None
        if hasattr(person, "wife"):
            second_half = person.wife
        elif hasattr(person, "husband"):
            second_half = person.husband
        if second_half:
            for num in seen:
                if person in num or second_half in num:
                    break
            else:
                seen.add(
                    (
                        person,
                        second_half,
                    )
                )
    return list(seen)


def main() -> None:
    people = [
        {"name": "Ross", "age": 30, "wife": "Rachel"},
        {"name": "Joey", "age": 29, "wife": None},
        {"name": "Rachel", "age": 28, "husband": "Ross"},
        {"name": "Hally", "age": 30, "husband": None},
        {"name": "Sue", "age": 29, "husband": "Rob"},
        {"name": "Rob", "age": 28, "wife": "Sue"},
    ]

    person_list = create_person_list(people)
    couples = get_married_couples(person_list)
    print(couples)
    previous = None
    for num in person_list:
        if previous:
            try:
                num.wedding(previous)
            except ValueError as error:
                print(error)
        if not num.is_married():
            previous = num
    couples = get_married_couples(person_list)
    print(couples)


if __name__ == "__main__":
    main()
