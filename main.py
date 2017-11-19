from activity_monitor.cpu import CpuMonitor
from activity_monitor.memory import MemoryMonitor
from config import CPUConstants
import time
from  datetime import datetime
from core.notification import Notification




def service():
    cpu_monitor = CpuMonitor(threshold_low=CPUConstants.low.value, threshold_high=CPUConstants.high.value,
                             activity_name='cpu', current_value=0)
    mem_monitor = MemoryMonitor(threshold_low=CPUConstants.low.value, threshold_high=CPUConstants.high.value,
                                activity_name='memory', current_value=0)
    while (True):
        print('sleeping at {0} !'.format(datetime.now()))
        time.sleep(5)
        print('woke up at {0} !'.format(datetime.now()))
        cpu_activity = cpu_monitor.monitor_activity()
        mem_activity = mem_monitor.monitor_activity()
        Notification.send_notifications([mem_activity, cpu_activity])


if __name__ == '__main__':
    service()







