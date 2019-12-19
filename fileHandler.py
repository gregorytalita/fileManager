from watchdog.events import FileSystemEventHandler
import os 

class FileHandler(FileSystemEventHandler):
  tracked_folder = ''
  destination_folder = ''

  def __init__(self, tracked, destination): 
    self.tracked_folder = tracked
    self.destination_folder = destination
  
  def on_modified(self, event):
    for filename in os.listdir(self.tracked_folder):
      src = self.tracked_folder + '/' + filename
      file_extension = os.path.splitext(filename)[1][1:]
      new_destination_folder = f'{self.destination_folder}/{file_extension}'
      new_destination = f'{new_destination_folder}/{filename}'

      if os.path.exists(new_destination_folder) == False:
        os.makedirs(new_destination_folder)

      os.rename(src, new_destination) 
