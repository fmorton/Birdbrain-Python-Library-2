from birdbrain.hummingbird import Hummingbird
from birdbrain.tasks import Tasks

import asyncio
import random


async def random_blinker(hummingbird):
    for i in range(35):
        hummingbird.tri_led(1, random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))

        await Tasks.yield_task()

    return "random_blinker"  # return is optional


async def blue_blinker(hummingbird):
    for i in range(35):
        hummingbird.tri_led(1, 0, 0, 100)

        await Tasks.yield_task()


hummingbird = Hummingbird('A')

tasks = Tasks()

tasks.create_task(random_blinker(hummingbird))
tasks.create_task(blue_blinker(hummingbird))

tasks.run()

random_blinker_result = tasks.result("random_blinker")

hummingbird.tri_led(1, 0, 0, 0)
