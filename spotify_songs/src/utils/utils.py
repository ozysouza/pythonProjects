import re

from datetime import date


def validate_date(date_input: str) -> bool:
    try:
        date.fromisoformat(date_input)
        return True
    except ValueError:
        return False


def clean_author_name(author_name: str) -> str:
    """
    Cleans the author name by replacing 'featuring' (or variants) with a semicolon.

    Args:
        author_name (str): The original author name.

    Returns:
        str: The cleaned author name.
    """
    # Replace variations of 'featuring' with a semicolon
    cleaned_name = re.sub(r'\b(featuring|feat\.|ft\.)\b', ',', author_name, flags=re.IGNORECASE)
    return cleaned_name.strip()
