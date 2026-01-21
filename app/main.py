from fastapi import FastAPI, HTTPException, Body
from services.call_logs import create_call_log

app = FastAPI(title="Firestore Call Logs API")


@app.post("/call-logs")
async def store_call_log(
    payload: dict = Body(
        ...,
        example={
            "call_metadata": {
                "room_name": "console",
                "timestamp": "2026-01-19T15:54:24.284769",
                "start_time": "2026-01-19T15:52:09.877976",
                "end_time": "2026-01-19T15:54:20.243795",
                "duration_seconds": 130.4,
                "message_count": 27
            },
            "contact_info": {
                "decision_maker_confirmed": True,
                "contact_person": "Marshal",
                "bank_name": None,
                "phone": None,
                "email": None
            },
            "call_analysis": {
                "status": {
                    "lead_score": 60,
                    "lead_quality": "Warm",
                    "lead_status": "Contacted",
                    "sales_stage": "Interest"
                },
                "engagement_metrics": {
                    "sentiment": "Neutral",
                    "interest_level": "Medium",
                    "language_used": "Hindi",
                    "call_quality": "Average"
                },
                "sales_intelligence": {
                    "win_probability": 50,
                    "pain_points_identified": ["Price"],
                    "objections_raised": ["Pricing concerns"],
                    "recommended_strategy": "Provide competitive pricing"
                },
                "call_outcome": {
                    "result": "Send Info",
                    "relationship_status": "Door Open"
                }
            },
            "call_summary": "Marshal inquired about pricing.",
            "schedule_meeting": {
                "action_required": True,
                "suggested_time_slots": ["2026-01-20T10:00:00"]
            }
        }
    ),
    database: str = "lumiverse-solutions"   # 🔥 dynamic DB via query param
):
    try:
        call_log = create_call_log(payload, database)

        return {
            "success": True,
            "call_log_id": call_log.id,
            "database": database,
            "message": "Call log stored successfully",
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Missing field: {e}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
