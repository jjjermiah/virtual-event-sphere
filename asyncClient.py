import asyncio
import aiohttp
from typing import Dict

class AsyncAPIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def _create_user_async(self, user_data: Dict):
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}/users/"
            async with session.post(url, json=user_data) as response:
                return await response.json(), response.status

    async def _create_multiple_users_async(self, user_data: Dict, n: int):
        tasks = []
        for _ in range(n):
            tasks.append(self._create_user_async(user_data))
        return await asyncio.gather(*tasks)
    
    def create_user(self, user_data: Dict):
        """Synchronous wrapper for the async '_create_user_async' method."""
        return asyncio.run(self._create_user_async(user_data))
    
    def create_multiple_users(self, user_data: Dict, n: int):
        """Synchronous wrapper for the async '_create_user_async' method."""
        return asyncio.run(self._create_multiple_users_async(user_data, n))

# Example usage
def main():
    client = AsyncAPIClient("http://127.0.0.1:8000/api")
    user_data = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "john.doe@example.com"
    }

    # Synchronous call to asynchronous method
    result, status = client.create_user(user_data)
    print(f"Result: {result}, Status: {status}")


def main2():
    client = AsyncAPIClient("http://127.0.0.1:8000/api")
    user_data = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "john.doe@example.com"
    }
    
    results = client.create_multiple_users(user_data, 3)
    for result, status in results:
        print(f"Result: {result}, Status: {status}")

    
if __name__ == "__main__":
    main2()