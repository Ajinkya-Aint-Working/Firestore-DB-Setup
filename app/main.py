from fastapi import FastAPI, HTTPException, Request
from services.call_logs import create_call_log

app = FastAPI(title="Firestore Call Logs API")


@app.post("/call-logs")
async def store_call_log(request: Request):
    try:
        payload = await request.json()
        call_log = create_call_log(payload)

        return {
            "success": True,
            "call_log_id": call_log.id,
            "message": "Call log stored successfully",
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Missing field: {e}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
