REQUIRED_CALL_ANALYSIS_KEYS = {
    "status",
    "engagement_metrics",
    "sales_intelligence",
    "call_outcome",
}

def build_call_analysis(data: dict) -> dict:
    missing = REQUIRED_CALL_ANALYSIS_KEYS - data.keys()
    extra = data.keys() - REQUIRED_CALL_ANALYSIS_KEYS

    if missing:
        raise ValueError(f"Missing call_analysis keys: {missing}")

    if extra:
        raise ValueError(f"Unexpected call_analysis keys: {extra}")

    return data
