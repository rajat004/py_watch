from enum import Enum

class CPUConstants(Enum):
    high = 40
    low = 0

class MemConstants(Enum):
    high = 80
    low = 0

class MeasuringInterval(Enum):
    cpu = 0
    memory = 0

class ActivityNames(Enum):
    cpu = 'cpu'
    memory = 'memory'

REST_INTERVAL = 3