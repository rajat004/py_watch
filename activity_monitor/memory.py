from core.Monitor import Monitor
from psutil import virtual_memory
import logging
from utils import Activity
from datetime import datetime
from config import ActivityNames

logger = logging.getLogger(__name__)


class MemoryMonitor(Monitor):

    '''
        monitoring  memory activity 
        can also provide highest mem
        consuming process generic 
        method needed.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def monitor_activity(self):
        logger.info('Started monitoring overall memory utilization at {0}'.format(datetime.now()))
        try:
            undesired_flag = -1
            memory_info = virtual_memory()
            self.current_value = memory_info.percent
            if self.activity_name is None:
                self.activity_name = ActivityNames.memory.value
            if self.current_value >= self.threshold_high:
                undesired_flag = 1
            elif self.current_value < self.threshold_low:
                undesired_flag = 0
            if undesired_flag > -1:
                return Activity(name= ActivityNames.memory.value, utilization= self.current_value)
        except Exception as E:
            logger.error(E)
            return None
        return None

    def get_most_memory_consuming_process(self):
        pass