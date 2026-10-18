VALID_STATUSES = ["applied", "interviewing", "offer", "rejected", "withdrawn"]

def validate_company(company):
    company = company.strip()

    if company == "":
        return False, "Company name cannot be empty"
    return True, ""

print(validate_company("miffy"))
print(validate_company(""))
print(validate_company("   "))

def clean_status(status):
    return status.strip().lower()

def validate_status(status):
    status = clean_status(status)

    if status == "":
        return False, "Status cannot be empty"
    elif status not in VALID_STATUSES:
        return False, "Status must be one of: " + ", ".join(VALID_STATUSES)
    return True, ""

print(validate_status("applied"))
print(validate_status(" Interviewing "))
print(validate_status("ghosted rip"))