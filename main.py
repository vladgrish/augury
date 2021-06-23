from Aggregator import Aggregator

if __name__ == "__main__":
    """
    Here we simply loop over all of the machines and their queues one by one.
    The assumption is that we are able to fullfil the task in under an hour
    Otherwise a different approach is needed. maybe async functionality to read\write from fs or a priority queue
    
    *given more time, I would probably use a more sophisticated method to manage the queue
    and also would wrap Aggregator and Queue Manager with FastAPI and put into separate containers
    I also wouldn't use classes at all if not required by task, the separation to modules is enough imho.
    All of the data could be stored in JSON fomat and transmited over REST
    """
    agg = Aggregator()
    while True:
        agg.aggregate()
        # or agg.aggregate_with_lag()
