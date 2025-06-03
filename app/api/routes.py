from fastapi import APIRouter
from datetime import datetime
import time

"""
    Build the services
"""


router = APIRouter()


"""
    Status API
    Returns the status of the API
    Returns the response time in milliseconds
"""
@router.get("/status")
async def status() -> dict:
    start_time = time.time()
    result = {      
        "status": "OK",
        "timestamp": datetime.now().isoformat()
    }
    end_time = time.time()
    result["response_time_ms"] = round((end_time - start_time) * 1000, 2)
    return result
