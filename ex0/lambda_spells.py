def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda m: m["power"], mages))
    return {
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": round(sum(powers) / len(powers), 2)
    }


if __name__ == "__main__":

    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
        {"name": "Fire Staff", "power": 92, "type": "staff"},
        {"name": "Ice Wand", "power": 78, "type": "wand"},
    ]

    mages = [
        {"name": "Merlin", "power": 100, "element": "fire"},
        {"name": "Gandalf", "power": 80, "element": "light"},
        {"name": "Morgana", "power": 60, "element": "shadow"},
    ]

    spells = ["fireball", "heal", "shield"]

    print("=== Artifact Sorter ===")
    print(artifact_sorter(artifacts))

    print("\n=== Power Filter ===")
    print(power_filter(mages, 75))

    print("\n=== Spell Transformer ===")
    print(spell_transformer(spells))

    print("\n=== Mage Stats ===")
    print(mage_stats(mages))
