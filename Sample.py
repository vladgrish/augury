from datetime import datetime
from dataclasses import dataclass

@dataclass
class Sample:    
    machine_id: str
    ep_id: str
    mesurement_time: datetime.timestamp
    mesurement_value: int