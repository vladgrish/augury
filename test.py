from Sample_Queue_manager import Sample_Queue_Manager
from Sample import Sample
from datetime import datetime
from pprint import pprint
import random

# Just a test to see the structure is fine and persist() works


sqm = Sample_Queue_Manager()
pprint(sqm.get_sample_queues())
for i in range(10):
    sqm.put_sample(Sample(random.choice(['machine1', 'machine2']), random.choice(['ep1', 'ep2']), datetime.timestamp(datetime.now()) + i*60*60, random.randint(10, 50)))
    sqm.put_sample(Sample(random.choice(['machine1', 'machine2']), random.choice(['ep1', 'ep2']), datetime.timestamp(datetime.now()) + i*60*60, random.randint(50, 90)))
print("\n"*3)
pprint(sqm.get_sample_queues())
