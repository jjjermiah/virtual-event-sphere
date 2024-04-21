from ves.schemas import (
    CreateEvent,
    EventOut,
)

from fastapi import (
    APIRouter, 
    HTTPException,
    Path,
)
from ves.crud import (
    create_event, 
    get_event_by_name, 
    get_all_events,
)

router = APIRouter()

@router.post("/events/", response_model=CreateEvent)
async def create_event_route(event: CreateEvent) -> EventOut:
    try:
        new_event = await create_event(event)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    return new_event

@router.get("/events/{name}", response_model=EventOut)
async def get_event_by_name_route(
    name: str = Path(default=..., title="Event Name")
) -> EventOut:
    event = await get_event_by_name(name)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.get("/events/", response_model=list[EventOut])
async def get_all_events_route() -> list[EventOut]:
    return await get_all_events()

