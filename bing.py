import asyncio

from sydney import SydneyClient


async def main() -> None:
    sydney = SydneyClient(style="balanced")

    await sydney.start_conversation()

    response = await sydney.compose("Why Python is a great language", format="ideas")
    print(response)

    await sydney.close_conversation()


if __name__ == "__main__":
    asyncio.run(main())