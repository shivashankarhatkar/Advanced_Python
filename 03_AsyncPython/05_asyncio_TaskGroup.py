"""
==============================================================================
CHAPTER: Advanced Asynchronous Python - Modern Task Management
==============================================================================
Topic: asyncio.TaskGroup (Introduced in Python 3.11)

What it does:
  - Manages multiple concurrent asynchronous tasks as a unified group.
  - Acts as a safer, modern alternative to 'asyncio.gather()'.

Why we use it (The Superpower):
  - Strict Error Handling: If one task in the group fails (raises an exception), 
    the TaskGroup automatically cancels all other running tasks in the group.
  - Clean Structure: Uses the 'async with' context manager, ensuring all 
    tasks are completely finished or cleaned up before the code moves forward.
==============================================================================
"""

import asyncio

async def fetch_data(server_id, delay):
    print(filename:=f"Starting download from Server {server_id}...")
    await asyncio.sleep(delay)  # Simulating a network delay
    print(f"✅ Finished Server {server_id}!")
    return f"Data from {server_id}"

async def main():
    # task_group manages multiple coroutines safely
    async with asyncio.TaskGroup() as tg:
        # We "create" tasks inside the group, and they start running immediately
        task1 = tg.create_task(fetch_data("A", 2))
        task2 = tg.create_task(fetch_data("B", 1))
    
    # Once the 'async with' block finishes, all tasks are guaranteed to be done
    print(f"Results gathered: {task1.result()}, {task2.result()}")

# To run the code:
asyncio.run(main())
