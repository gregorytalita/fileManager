from watchdog.observers import Observer

import os 
import json
import time

from fileHandler import FileHandler

tracked_folder = input('Type the path to the folder to be tracked: \n')
destination_folder = input('Type the path to the destination folder: \n')

event_handler = FileHandler(tracked_folder, destination_folder)
observer = Observer()
observer.schedule(event_handler, tracked_folder, recursive=True)
observer.start()

try:
  while True:
    time.sleep(10)
except KeyboardInterrupt:
  observer.stop()

observer.join()
