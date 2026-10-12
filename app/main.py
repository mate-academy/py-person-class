class RockBand:
    def __init__(self, name: str, members: list[str]) -> None:
        self.name = name
        self.members = members

    def add_new_member(self, new_member: str) -> None:
        if new_member in self.members:
            print(f"{new_member} is already in the band!")
        else:
            self.members.append(new_member)

    def __add__(self, other: "RockBand") -> "RockBand":
        combined_name = f"{self.name} {other.name} United"
        combined_members = []
        for member in self.members + other.members:
            if member not in combined_members:
                combined_members.append(member)
        return RockBand(name=combined_name, members=combined_members)
