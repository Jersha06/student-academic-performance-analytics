import logging
from pathlib import Path


def configure_logging():
    Path("logs").mkdir(exist_ok=True)

    logging.basicConfig(
        filename="logs/application.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


def validate_non_empty_string(value, field_name):
    """Validate that a value is a non-empty string."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} cannot be empty.")

    return value.strip()


def validate_range(value, field_name, minimum=0, maximum=100):
    """Validate that a numeric value is within a specified range."""
    try:
        value = float(value)
    except (TypeError, ValueError):
        raise ValueError(f"{field_name} must be a number.")

    if value < minimum or value > maximum:
        raise ValueError(
            f"{field_name} must be between {minimum} and {maximum}."
        )

    return value


def safe_int(value, minimum=None, maximum=None):
    """Convert a value to integer and optionally validate its range."""
    number = int(value)

    if minimum is not None and number < minimum:
        raise ValueError(f"Value must be >= {minimum}")

    if maximum is not None and number > maximum:
        raise ValueError(f"Value must be <= {maximum}")

    return number