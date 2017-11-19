from activity_monitor.cpu import CpuMonitor
from activity_monitor.memory import MemoryMonitor
from config import CPUConstants, MemConstants, ActivityNames, REST_INTERVAL
import time
from  datetime import datetime
from core.notification import Notification
import logging

logger = logging.getLogger(__name__)



def service():
    cpu_monitor = CpuMonitor(threshold_low=CPUConstants.low.value, threshold_high=CPUConstants.high.value,
                             activity_name=ActivityNames.cpu.value, current_value=0)
    mem_monitor = MemoryMonitor(threshold_low=MemConstants.low.value, threshold_high=MemConstants.high.value,
                                activity_name=ActivityNames.memory.value, current_value=0)
    while(True):
        logger.info('sleeping at {0} !'.format(datetime.now()))
        time.sleep(REST_INTERVAL)
        logger.info('woke up at {0} !'.format(datetime.now()))
        cpu_activity = cpu_monitor.monitor_activity()
        mem_activity = mem_monitor.monitor_activity()
        Notification.send_notifications([mem_activity, cpu_activity])

if __name__ == '__main__':
    service()







