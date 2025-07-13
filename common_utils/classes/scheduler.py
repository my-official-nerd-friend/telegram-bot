import schedule
import time
import threading

class Scheduler:
    def __init__(self):
        self.thread = threading.Thread(target=self._run, daemon=True)
        self.running = False

    def start(self):
        self.running = True
        self.thread.start()

    def _run(self):
        while self.running:
            schedule.run_pending()
            time.sleep(1)

    def stop(self):
        self.running = False

    def schedule_task_in_seconds(self, interval, func):
        schedule.every(interval).seconds.do(func)
    
    def schedule_task_in_minutes(self, interval, func):
        schedule.every(interval).minutes.do(func)
    
    def schedule_task_in_hours(self, interval, func):
        schedule.every(interval).hours.do(func)