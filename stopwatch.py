import time

"""
Program 3:Write a Stopwatch Program for measuring the time that elapses between
the start and end clicks
"""

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60

    print("Time Lapsed = {0}:{1}:{2}".format(hours, mins, sec))


input("press enter to start: ")
start_time = time.time()
input("press enter to stop: ")
end_time = time.time()
time_lapsed = end_time - start_time

if __name__ == '__main__':
    time_convert(time_lapsed)
