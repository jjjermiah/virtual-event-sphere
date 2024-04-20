import asyncio
import aiohttp
import json

async def create_user(session, data):
    async with session.post("http://127.0.0.1:8000/api/users/", data=json.dumps(data), headers={"Content-Type": "application/json"}) as response:
        print(await response.text())

async def main():
    async with aiohttp.ClientSession() as session:
        user1 = {"name": "John Doe", "username": "johndoe", "email": "john.doe@example.com"}
        user2 = {"name": "Jane Doe", "username": "janedoe", "email": "jane.doe@example.com"}
        await asyncio.gather(
            create_user(session, user1),
            create_user(session, user2)
        )

if __name__ == "__main__":
    asyncio.run(main())