session_state = {
    "search_goal": None,
    "deadline": None,
    "application_count": 0,
    "current_pipeline": [],
    "last_action_taken": None,
}

def create_application(company_name, role_title, date_applied, current_status="applied", notes=""):
    return {
        "company_name": company_name,
        "role_title": role_title,
        "date_applied": date_applied,
        "current_status": current_status,
        "notes": notes,
}