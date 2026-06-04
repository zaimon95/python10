from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import Any, Callable


def spell_reducer(spell_list: list[int], operation: str) -> int:
    if not spell_list:
        return 0

    ops: dict[str, Callable] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }

    if operation not in ops:
        raise ValueError("Unknown operation")

    return reduce(ops[operation], spell_list)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "lightning": partial(base_enchantment, 50, "lightning"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def dispatch(arg):
        return "Unknown spell type"

    @dispatch.register
    def _(arg: int):
        return f"Damage spell: {arg} damage"

    @dispatch.register
    def _(arg: str):
        return f"Enchantment: {arg}"

    @dispatch.register
    def _(arg: list):
        return f"Multi-cast: {len(arg)} spells"

    return dispatch


if __name__ == "__main__":
    print("=== Spell Reducer ===")

    spells = [10, 20, 30, 40]

    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    print(f"Min: {spell_reducer(spells, 'min')}")

    print("\n=== Partial Enchanter ===")

    def enchant(power: int, element: str, target: str) -> str:
        return f"{element} enchantment ({power}) on {target}"

    enchantments = partial_enchanter(enchant)

    print(enchantments["fire"]("Sword"))
    print(enchantments["ice"]("Shield"))
    print(enchantments["lightning"]("Hammer"))

    print("\n=== Fibonacci ===")

    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\n=== Spell Dispatcher ===")

    dispatcher = spell_dispatcher()

    print(dispatcher(50))
    print(dispatcher("fireball"))
    print(dispatcher(["fireball", "heal"]))
    print(dispatcher({"unknown": True}))
