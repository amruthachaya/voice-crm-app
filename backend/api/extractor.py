import re

NUMBER_MAP = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "double": "2",
    "triple": "3"
}

def normalize_numbers(text: str) -> str:
    """
    Converts spoken numbers to digits.
    Example:
    'nine nine eight eight seven seven six six five five'
    -> '9988776655'
    """
    words = text.lower().split()
    result = []
    i = 0

    while i < len(words):
        if words[i] == "double" and i + 1 < len(words):
            digit = NUMBER_MAP.get(words[i + 1])
            if digit:
                result.append(digit * 2)
                i += 2
                continue
        if words[i] in NUMBER_MAP:
            result.append(NUMBER_MAP[words[i]])
        i += 1

    return "".join(result)


def extract_phone(text: str) -> str | None:
    normalized = normalize_numbers(text)

    match = re.search(r"\b\d{10}\b", normalized)
    if match:
        return match.group()
    return None


def extract_name(text: str) -> str | None:
    patterns = [
        r"customer ([A-Z][a-z]+ [A-Z][a-z]+)",
        r"with ([A-Z][a-z]+ [A-Z][a-z]+)",
        r"spoke with ([A-Z][a-z]+ [A-Z][a-z]+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1)

    return None

def extract_address(text: str) -> dict:
    address = None
    city = None
    locality = None

    address_match = re.search(r"stays at (.*?)[.,]", text, re.IGNORECASE)
    if address_match:
        address = address_match.group(1)

    city_match = re.search(r",\s*([A-Z][a-z]+)$", text)
    if city_match:
        city = city_match.group(1)

    locality_match = re.search(r",\s*([A-Z][a-z ]+),", text)
    if locality_match:
        locality = locality_match.group(1)

    return {
        "address": address,
        "city": city,
        "locality": locality
    }


def extract_summary(text: str) -> str:
    summary_match = re.search(r"we discussed (.*)", text, re.IGNORECASE)
    if summary_match:
        return summary_match.group(1).strip()
    return "General customer interaction"

from datetime import datetime

def extract_entities(transcript: str) -> dict:
    phone = extract_phone(transcript)
    name = extract_name(transcript)
    address_data = extract_address(transcript)
    summary = extract_summary(transcript)

    return {
        "customer": {
            "full_name": name,
            "phone": phone,
            "address": address_data["address"],
            "city": address_data["city"],
            "locality": address_data["locality"],
        },
        "interaction": {
            "summary": summary,
            "created_at": datetime.utcnow().isoformat()
        }
    }

