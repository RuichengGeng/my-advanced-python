async io is very extensively used in my life, even much more than multi-thread or multi-process.
The most used cases is: get data from vander - populate data into db - at the same time do model calibration, so let's just practice this case
### Before going to details of async io operation, its necessary for me to refresh some backgroup knowledge about:
1. Parallelism vs Concurrency:
   1. In one words: concurrency is just tasks happened at the same time, parallelism is tasks are being done at the same time
   2. [difference-between-concurrency-and-parallelism](https://www.geeksforgeeks.org/difference-between-concurrency-and-parallelism/)
2. Thread vs Process and asyncio
   1. Might not be accurate in my words: just see this link: [asyncio-threading-and-multiprocessing-in-python](https://medium.com/analytics-vidhya/asyncio-threading-and-multiprocessing-in-python-4f5ff6ca75e8)
   2. I like [this post](https://itnext.io/practical-guide-to-async-threading-multiprocessing-958e57d7bbb8)



#### Here are some useful links below:
- [watch this video before reading anything](https://www.youtube.com/watch?v=t5Bo1Je9EmE)
- [intro-async-io](https://realpython.com/async-io-python/)
