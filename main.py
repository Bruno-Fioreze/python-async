
from pprint import pprint
import asyncio

async def concat_name(first_name: str, last_name: str):
    print(f"name : {first_name} {last_name}")
    return f"{first_name} {last_name}"


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

async def main():
    names = [
        {"first_name": "Bruno", "last_name": "Fioreze"},
        {"first_name": "Jaona", "last_name": "Fioreze"},
        {"first_name": "Fernanda", "last_name": "Fioreze"},
        {"first_name": "Bruna", "last_name": "Fioreze"},
        {"first_name": "Maria", "last_name": "Fioreze"},
        {"first_name": "Eduarda", "last_name": "Fioreze"},
        {"first_name": "Giovanna", "last_name": "Fioreze"},
        {"first_name": "Lara", "last_name": "Fioreze"},
        {"first_name": "Larrisa", "last_name": "Fioreze"},
        {"first_name": "Gabi", "last_name": "Fioreze"},
        {"first_name": "Manuela", "last_name": "Fioreze"},
    ]

    for name in names:
        first_name, last_name = name["first_name"], name["last_name"]
        count_active_tasks = len(asyncio.all_tasks())
        if count_active_tasks == 5:
            number_tasks_actives = len(asyncio.all_tasks())
            while number_tasks_actives >= 2:
                print(f"number_tasks_actives: {number_tasks_actives}")
                await asyncio.sleep(60)
                number_tasks_actives = len(asyncio.all_tasks())
        loop.create_task(
            concat_name(first_name=first_name, last_name=last_name)
        )

loop.run_until_complete(main())