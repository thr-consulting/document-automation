import asyncio
from bullmq import Worker, Queue 
import os
from dotenv import load_dotenv
load_dotenv() 

from workflow import workflow

async def doSomethingAsync(job, job_token):
    print("\n---\nreceived job: {}".format(job.id))
    print("job name: {}".format(job.name))
    print("job data: {}".format(job.data))
    result = 'hello ' + str(job.data)
    result = workflow(job.data['url'], job.data['id'])
    if result:
        queue = Queue('processorQueue', {"connection": os.getenv('REDIS_URL'), "prefix": "tacs", "removeOnComplete": True})
        job = await queue.add("sorted_job", result)
        print("added job to processorQueue: {}".format(job.id))
        return result

    return "Nothing to return"

async def main():
    print("Waiting for jobs")
    Worker("sortFileQueue", doSomethingAsync, {"connection": os.getenv('REDIS_URL'), "prefix": "tacs"})

    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())