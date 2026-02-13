import asyncio
import os
from pyrogram import Client


def get_input(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\nProcess Cancelled ❌")
        exit()


async def generate_string():
    print("\n🎵 KAIxGenMusic - Pyrogram String Generator\n")

    api_id = get_input("Enter Your API_ID: ")
    api_hash = get_input("Enter Your API_HASH: ")

    async with Client(
        name="KAIxGenSession",
        api_id=int(api_id),
        api_hash=api_hash,
        in_memory=True,
    ) as app:

        string_session = await app.export_session_string()

        print("\n✅ STRING SESSION GENERATED SUCCESSFULLY!\n")
        print("⚠️ Keep this secret. Do NOT share with anyone.\n")
        print(string_session)

        try:
            await app.send_message(
                "me",
                f"🎵 KAIxGenMusic String Session:\n\n`{string_session}`"
            )
        except Exception:
            pass


if __name__ == "__main__":
    asyncio.run(generate_string())
