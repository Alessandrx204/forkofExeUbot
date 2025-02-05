import asyncio

async def loading_animation(event, message, duration=5, interval=0.5):
    animation_chars = ["⠋", "⠙", "⠹", "⠽", "⠿", "⠃"]
    end_time = asyncio.get_event_loop().time() + duration
    while asyncio.get_event_loop().time() < end_time:
        for char in animation_chars:
            await event.edit(f"{char} {message}")
            await asyncio.sleep(interval)
