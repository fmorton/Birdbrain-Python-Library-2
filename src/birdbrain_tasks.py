import asyncio

class BirdbrainTasks:
    def __init__(self):
        self.method_list = []
        self.task_list = []
        self.results = {}
        
    def result(self, name):
        return self.results[name]

    def create_task(self, method):
        self.method_list.append(method)

    def run(self):
        asyncio.run(self.runner())

    def wait(self):
        pass

    async def runner(self):
        for method in self.method_list:
            self.task_list.append(asyncio.create_task(method))

        while True:
            running_task_count = 0

            for task in self.task_list:
                try:
                    self.results[task.get_coro().__name__] = task.result()
                except asyncio.exceptions.InvalidStateError:
                    pass

                if not task.done(): running_task_count += 1

            if running_task_count == 0: break

            await self.yield_task()

    @classmethod
    async def yield_task(self, yield_time = 0.0):
        await asyncio.sleep(yield_time)
