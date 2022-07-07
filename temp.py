#importing stuff
import threading
import os

       time = input("how often would you like the refresh rate to be  ")
def printit():
	 threading.Timer(time, printit().start()
	 os.system("clear")
	 os.system("vcgencmd measure_temp")
printit()
except KeyboardInterrupt:
print("")
print("quitting...")
# this scriped is for the rasberry pi and uses the "vcgencmd measure_temp" command to get cpu TEMP
# made by nosson.p. a long long time ago.
