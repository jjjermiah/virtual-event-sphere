from asyncio import events
from ves.db import db

from ves.schemas import (
    CreateEvent,
    EventOut,
)

from typing import Optional


async def create_event(event: CreateEvent) -> EventOut:
    existing_event = await get_event_by_name(event.name)
    
    if existing_event:
        raise ValueError("Event already exists")
    
    new_event = event.model_dump()
    await db.events.insert_one(new_event)
    return EventOut(**new_event)

async def get_event_by_name(name: str) -> Optional[EventOut]:
    event = await db.events.find_one(
        filter={"name": name}
    )
    if event:
        return EventOut(**event)
    return None

async def get_all_events() -> list[EventOut]:
    events = await db.events.find().to_list(length=None)
    
    return [EventOut(**event) for event in events]

