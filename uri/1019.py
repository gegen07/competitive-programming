valor = int(input())

timesHours = int((valor-valor%3600)/3600)
valor -= timesHours * 3600

timesMinutes = int((valor-valor%60)/60)
valor -= timesMinutes * 60

print("{0}:{1}:{2}".format(timesHours, timesMinutes, valor))
