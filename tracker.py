session_state = {
    "search_goal": None,
    "deadline": None,
    "application_count": 0,
    "current_pipeline": [],
    "last_action_taken": None,
}

print(session_state)

application = {
    "company_name": "Miffy Tech",
    "role_title": "Chief Cuteness Officer",
    "date_applied": "2026-10-17",
    "current_status": "applied",
    "notes": "",
}
print(application)

def create_application(company_name, role_title, date_applied, current_status="applied", notes=""):
    return {
        "company_name": company_name,
        "role_title": role_title,
        "date_applied": date_applied,
        "current_status": current_status,
        "notes": notes,
    }

print(create_application("miffy", "cco", "2026-10-18"))
print(create_application("miffy", "chief cuteness officer", "2026-10-18", "interviewing", "felt cute while giving interview"))