from core.Monitor import Monitor
from psutil import cpu_percent
import logging
from config import ActivityNames
from utils import Activity
from core.notification import Notification
from datetime import datetime

logger = logging.getLogger(__name__)


class CpuMonitor(Monitor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def monitor_activity(self):
        logger.info('Started monitoring overall cpu utilization at {0}'.format(datetime.now()))
        try:
            undesired_flag = -1
            self.current_value = cpu_percent()
            if self.activity_name is None:
                self.activity_name = ActivityNames.cpu.value
            if self.current_value >= self.threshold_high:
                undesired_flag = 1
            elif self.current_value < self.threshold_low:
                undesired_flag = 0
            if undesired_flag > -1:
                return Activity(name= ActivityNames.cpu.value, utilization= self.current_value)
        except Exception as e:
            logger.error(e)
            return None
        return None

    def get_most_cpu_consuming_process(self):
        pass