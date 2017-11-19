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
        self.undesired_flag = None

    def monitor_activity(self):
        logger.info('Started monitoring overall cpu utilization at {0}'.format(datetime.now()))
        self.current_value = cpu_percent(1)
        if self.activity_name is None:
            self.activity_name = ActivityNames.cpu.value
        if self.current_value >= self.threshold_high:
            self.undesired_flag = 1
        elif self.current_value < self.threshold_low:
            self.undesired_flag = 0
        if self.undesired_flag is not None:
            return Activity(name= ActivityNames.cpu.value, utilization= self.current_value)
        return None

    def get_most_cpu_consuming_process(self):
        pass