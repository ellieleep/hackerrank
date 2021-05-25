TwelveHourTime = input()

timeSplit = TwelveHourTime.split(':')

hours = int(timeSplit[0])
minutes = int(timeSplit[1])
seconds = timeSplit[2]
isPM = False

if 'PM' in seconds:
    isPM = True

if hours == 12 and not isPM:
    hours = '00'

seconds = seconds.replace('PM', '')
seconds = seconds.replace('AM', '')

if isPM and hours != 12:
    hours += 12

if hours == 24:
    hours = '00'

print(str(hours).zfill(2) + ':' + str(minutes).zfill(2) + ':' + str(seconds).zfill(2))

