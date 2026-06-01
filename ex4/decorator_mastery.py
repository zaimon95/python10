from functools import wraps
import time
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func):
        @wraps(func)
        def wrapper(self, power, *args, **kwargs):
            if power >= min_power:
                return func(self, power, *args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... (attempt"
                          f"{attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":

    @spell_timer
    def fireball():
        time.sleep(1)
        return "Fireball cast!"

    print("=== Spell Timer ===")
    print(fireball())

    print("\n=== Retry Spell ===")

    attempts = 0

    @retry_spell(3)
    def unstable_spell():
        global attempts
        attempts += 1

        if attempts < 3:
            raise Exception

        return "Spell succeeded!"

    print(unstable_spell())

    print("\n=== Static Method ===")

    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("12"))

    print("\n=== Cast Spell ===")

    guild = MageGuild()

    print(guild.cast_spell(15, "Lightning"))
    print(guild.cast_spell(5, "Lightning"))
