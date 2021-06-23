import pickle
from Sample import Sample
from pathlib import Path
import os

class Sample_Queue_Manager():
    def __init__(self):
        try:
            self.sample_queues = {x: {} for x in os.listdir("queues/")}
            for machine in self.sample_queues:
                try:
                    for ep in os.listdir(f"queues/{machine}/"):
                        with open(f"queues/{machine}/{ep}", 'rb') as input:
                            print(f"reading machine: {machine}, ep: {ep}")
                            ep_queue = pickle.load(input)
                            print(f'got: {ep_queue}')
                            self.sample_queues[machine][ep] = ep_queue
                except:
                    self.sample_queues[machine] = {}
        except:
            Path("queues").mkdir(exist_ok=True)
            self.sample_queues = {}

    def persist(self, machine: str, ep: str):
        print(f"writing to: queues/{machine}/{ep}")
        with open(f"queues/{machine}/{ep}", 'wb') as output:
            pickle.dump(self.sample_queues[machine][ep], output, pickle.HIGHEST_PROTOCOL)

    def add_machine(self, machine: str):
        """add sub dir for specified machine

        Args:
            machine (Sample.machine_id): machine id
        """
        self.sample_queues[machine] = {}
        Path(f"queues/{machine}").mkdir(parents=True, exist_ok=True)
    
    def add_ep(self, machine: str, ep: str):
        """Add a queue for the specified end point

        Args:
            machine (Sample.machine_id): machine id
            ep (Sample.ep_id): end point id
        """
        try:
            self.sample_queues[machine][ep] = []
        except:
            self.add_machine(machine)
            self.sample_queues[machine][ep] = []
        
    
    def put_sample(self, sample: Sample):
        """add a set of {time, value} to the apropriate list

        Args:
            sample (Sample): a Sample
        """
        try:
            ep_queue = self.sample_queues[sample.machine_id][sample.ep_id]
        except:
            self.add_ep(sample.machine_id, sample.ep_id)
            ep_queue = self.sample_queues[sample.machine_id][sample.ep_id]
        
        ep_queue.append([sample.mesurement_time, sample.mesurement_value])
        self.persist(sample.machine_id, sample.ep_id)

    def get_sample_queues(self) -> dict:
        """get the dict with machines, eps, and queues

        Returns:
            dict: returns the complete structure
        """
        return self.sample_queues