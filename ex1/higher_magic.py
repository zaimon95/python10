from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int):
        return spell1(target, power), spell2(target, power)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int):
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int):
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int):
        return [spell(target, power) for spell in spells]
    return sequence


if __name__ == "__main__":

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power}"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power}"

    def strong_enough(target: str, power: int) -> bool:
        return power >= 20

    print("=== Spell Combiner ===")

    combo = spell_combiner(fireball, heal)
    print(combo("Dragon", 30))

    print("\n=== Power Amplifier ===")

    mega_fireball = power_amplifier(fireball, 3)
    print(mega_fireball("Dragon", 30))

    print("\n=== Conditional Caster ===")

    conditional = conditional_caster(strong_enough, fireball)

    print(conditional("Dragon", 10))
    print(conditional("Dragon", 30))

    print("\n=== Spell Sequence ===")

    sequence = spell_sequence([fireball, heal])
    print(sequence("Dragon", 20))
