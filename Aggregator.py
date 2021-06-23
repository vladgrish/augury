from Session import Session
from Sample_Queue_manager import Sample_Queue_Manager

class Aggregator:
    def __init__(self):
        qeueu_manager = Sample_Queue_Manager()
        self.queues = qeueu_manager.get_sample_queues()
        self.eps_lag = {}
        pass

    def aggregate(self):
        """ to aggregate without lag we simply wait untill both ep's have
        at least one sample to create a session containing them
        """
        for machine in self.queues:
            eps = [ep for ep in machine]
            if self.queues[machine][eps[0]].len() > 0 and self.queues[machine][eps[1]].len() > 0:
                print(Session(self.queues[machine][eps[0]].pop(), self.queues[machine][eps[1]].pop()))

    def aggregate_with_lag(self):
        """with lag the max samples per queue is 3,
        whenever we have more than 2 samples, we create a session with just,
        flag the other ep as lagging and address it in the future
        """
        for machine in self.queues:
            eps = [ep for ep in machine]
            if self.queues[machine][eps[0]].len() > 2:
                self.eps_lag[eps[1]] = 1
                sample1 = self.queues[machine][eps[0]].pop()
                sample2 = None
                print(Session(sample1, sample2))

            if self.queues[machine][eps[1]].len() > 2:
                self.eps_lag[eps[0]] = 1
                sample1 = None
                sample2 = self.queues[machine][eps[1]].pop()
                print(Session(sample1, sample2))

            if self.queues[machine][eps[0]].len() > 0 and self.queues[machine][eps[1]].len() > 0:
                sample1 = self.queues[machine][eps[0]].pop()
                sample2 = self.queues[machine][eps[1]].pop()
                if self.eps_lag[eps[0]] == 1:
                    self.eps_lag[eps[0]] = 0
                    sample1 = None
                if self.eps_lag[eps[1]] == 1:
                    self.eps_lag[eps[1]] = 0
                    sample2 = None
                print(Session(sample1, sample2))