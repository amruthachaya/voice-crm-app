TEST_CASES = [
    {
        "id": 1,
        "input": "I spoke with customer Amit Verma today. His phone number is 9988776655. He stays at 45 Park Street, Salt Lake, Kolkata. We discussed the demo and next steps.",
        "expected": {
            "full_name": "Amit Verma",
            "phone": "9988776655",
            "city": "Kolkata"
        }
    },
    {
        "id": 2,
        "input": "Today I spoke with customer Riya Sharma. Her number is 9987654321. She lives at MG Road, Bangalore.",
        "expected": {
            "full_name": "Riya Sharma",
            "phone": "9987654321",
            "city": "Bangalore"
        }
    }
]

