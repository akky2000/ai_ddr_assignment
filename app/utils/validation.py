def detect_conflicts(inspection_text, thermal_text):

    conflicts = []

    if "no moisture" in inspection_text.lower() and "moisture" in thermal_text.lower():
        conflicts.append(
            "Conflict detected: Inspection report says no moisture but thermal report indicates moisture."
        )

    if "no heat loss" in inspection_text.lower() and "heat loss" in thermal_text.lower():
        conflicts.append(
            "Conflict detected: Thermal report indicates heat loss but inspection report does not."
        )

    return conflicts

def detect_missing(data):

    missing = []

    for key, value in data.items():

        if value == "" or value is None:
            missing.append(f"{key} : Not Available")

    return missing

def remove_duplicates(observations):

    seen = set()
    result = []

    for obs in observations:

        text = obs["observation"]

        if text not in seen:
            seen.add(text)
            result.append(obs)

    return result