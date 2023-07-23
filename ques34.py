'''Create a class watch with hr, min, sec, alarm type and methods setAlarm, stopAlarm, showTime.'''

class Watch:
    def __init__(self, hr, min, sec, alarmHr=None, alarmMin=None, alarmType=None) :
        self.hr = hr
        self.min = min
        self.sec = sec
        self.alarmHr = alarmHr
        self.alarmMin = alarmMin
        self.alarmType = alarmType

    def setAlarm(self,alarmHr, alarmMin, alarmType) :
        self.alarmHr = alarmHr
        self.alarmMin = alarmMin
        self.alarmType = alarmType

    def showTime(self):
        print(f"Current Time:\t{self.hr}:{self.min}:{self.sec}")

watch = Watch(10,20,30)
watch.setAlarm(8,00,00)
watch.showTime()