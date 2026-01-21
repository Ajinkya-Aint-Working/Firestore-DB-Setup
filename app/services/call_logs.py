from datetime import datetime
from uuid import uuid4

from firestore import get_db
from models import CallLog, CallAnalysis
from services.utils import build_call_analysis

db = get_db()
call_logs_ref = db.collection("call_logs")


def create_call_log(payload: dict) -> CallLog:
    call_log_id = str(uuid4())

    analysis_data = build_call_analysis(payload["call_analysis"])

    call_analysis = CallAnalysis(
        status=analysis_data["status"],
        engagement_metrics=analysis_data["engagement_metrics"],
        sales_intelligence=analysis_data["sales_intelligence"],
        call_outcome=analysis_data["call_outcome"],
    )

    call_log = CallLog(
        id=call_log_id,
        call_metadata=payload["call_metadata"],
        contact_info=payload["contact_info"],
        call_analysis=call_analysis,
        call_summary=payload["call_summary"],
        schedule_meeting=payload["schedule_meeting"],
        created_at=datetime.utcnow(),
    )

    call_logs_ref.document(call_log.id).set(call_log.to_dict())
    return call_log
