from dataclasses import dataclass
from typing import Dict, List


@dataclass
class UserSettings:
    weekStart: str
    timeZone: str
    timeFormat: str
    dateFormat: str
    sendNewsletter: bool
    weeklyUpdates: bool
    longRunning: bool
    scheduledReports: bool
    approval: bool
    pto: bool
    alerts: bool
    reminders: bool
    timeTrackingManual: bool
    summaryReportSettings: Dict[str, str]
    isCompactViewOn: bool
    dashboardSelection: str
    dashboardViewType: str
    dashboardPinToTop: bool
    projectListCollapse: int
    collapseAllProjectLists: bool
    groupSimilarEntriesDisabled: bool
    myStartOfDay: str
    projectPickerTaskFilter: bool
    lang: str
    multiFactorEnabled: bool
    theme: str
    scheduling: bool
    onboarding: bool
    showOnlyWorkingDays: bool

@dataclass
class MeuUser:
    id: str
    email: str
    name: str
    memberships: List
    profilePicture: str
    activeWorkspace: str
    defaultWorkspace: str
    settings: UserSettings
    status: str
    customFields: List
   

    def __str__(self):
        return f"Usuário: {self.name} ({self.email}) | Status: {self.status} | Workspace: {self.activeWorkspace}"



def json_para_meu_user(data: dict) -> MeuUser:
    settings = UserSettings(**data["settings"])
    return MeuUser(
        id=data["id"],
        email=data["email"],
        name=data["name"],
        memberships=data["memberships"],
        profilePicture=data["profilePicture"],
        activeWorkspace=data["activeWorkspace"],
        defaultWorkspace=data["defaultWorkspace"],
        settings=settings,
        status=data["status"],
        customFields=data["customFields"]
        
    )