import pandas as pd
from .test_cases import TEST_CASES
from ..extractor import extract_entities


def evaluate_extraction():
    rows = []

    for case in TEST_CASES:
        extracted = extract_entities(case["input"])

        row = {
            "test_id": case["id"],
            "input_text": case["input"],
            "expected_name": case["expected"].get("full_name"),
            "actual_name": extracted["customer"]["full_name"],
            "expected_phone": case["expected"].get("phone"),
            "actual_phone": extracted["customer"]["phone"],
            "expected_city": case["expected"].get("city"),
            "actual_city": extracted["customer"]["city"],
            "hitl_verified": False
        }

        rows.append(row)

    return pd.DataFrame(rows)

def generate_excel_report(file_path="evaluation_results.xlsx"):
    df = evaluate_extraction()
    df.to_excel(file_path, index=False)
    return file_path
