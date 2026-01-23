from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict


# ---------------- Call Analysis ----------------
@dataclass
class CallAnalysis:
    status: Dict[str, Any]
    engagement_metrics: Dict[str, Any]
    sales_intelligence: Dict[str, Any]
    next_steps: Dict[str, Any]
    call_outcome: Dict[str, Any]

    def to_dict(self):
        return {
            "status": self.status,
            "engagement_metrics": self.engagement_metrics,
            "sales_intelligence": self.sales_intelligence,
            "next_steps": self.next_steps,
            "call_outcome": self.call_outcome,
        }


# ---------------- Call Log ----------------
@dataclass
class CallLog:
    id: str
    call_metadata: Dict[str, Any]
    contact_info: Dict[str, Any]
    call_analysis: CallAnalysis
    call_summary: str
    schedule_meeting: Dict[str, Any]
    created_at: datetime

    def to_dict(self):
        return {
            "call_metadata": self.call_metadata,
            "contact_info": self.contact_info,
            "call_analysis": self.call_analysis.to_dict(),
            "call_summary": self.call_summary,
            "schedule_meeting": self.schedule_meeting,
            "created_at": self.created_at,
        }
