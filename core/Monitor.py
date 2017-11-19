from utils import Activity

class Monitor:
    '''
        Base class to define set of 
        rules for monitoring activity
        it is recommended for any new 
        activity to inherit this class.
    
    '''
    def __init__(self, threshold_high: float, threshold_low: float, current_value: float, activity_name: str):
        self._threshold_high = threshold_high
        self._threshold_low = threshold_low
        self._current_value = current_value
        self._activity_name = activity_name

    @property
    def threshold_high(self):
        return self._threshold_high

    @property
    def threshold_low(self):
        return self._threshold_low

    @property
    def current_value(self):
        return self._current_value

    @property
    def activity_name(self):
        return self._activity_name

    @current_value.setter
    def current_value(self, value: float= None):
        self._current_value = value

    @activity_name.setter
    def set_activity_name(self, name: str= None):
        self._activity_name = name

    def monitor_activity(self) -> Activity:
        pass

    def send_notifications(self) -> bool:
        pass
