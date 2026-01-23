from datetime import datetime
from uuid import uuid4

from firestore import get_db
from models import CallLog, CallAnalysis
from services.utils import build_call_analysis


def create_call_log(payload: dict, database: str) -> CallLog:
    # 🔥 dynamic database
    db = get_db(database)
    call_logs_ref = db.collection("call_logs")

    call_log_id = str(uuid4())

    analysis_data = build_call_analysis(payload["call_analysis"])

    call_analysis = CallAnalysis(
        status=analysis_data["status"],
        engagement_metrics=analysis_data["engagement_metrics"],
        sales_intelligence=analysis_data["sales_intelligence"],
        next_steps=analysis_data["next_steps"],
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

    # Document ID is reference, not stored inside document
    call_logs_ref.document(call_log.id).set(call_log.to_dict())

    return call_log


# ---------------- GET BY ID ----------------
def get_call_log_by_id(call_log_id: str, database: str) -> dict:
    db = get_db(database)
    doc_ref = db.collection("call_logs").document(call_log_id)
    doc = doc_ref.get()

    if not doc.exists:
        return None

    return {
        "id": call_log_id,
        **doc.to_dict()
    }


# ---------------- LIST ----------------
def list_call_logs(database: str, limit: int = 20) -> list:
    db = get_db(database)
    query = (
        db.collection("call_logs")
        .order_by("created_at", direction="DESCENDING")
        .limit(limit)
    )

    results = []
    for doc in query.stream():
        results.append({
            "id": doc.id,
            **doc.to_dict()
        })

    return results