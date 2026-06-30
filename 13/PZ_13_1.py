'''
В исходном текстовом файле (radio stations.txt) найти все домены из URL-адресов
(HanpиMep, B URL-a pece http://stream.hoster.by:8081/pilotfn/audio/icecast.audio домен
выделен полужирным).
'''

import re
with open("radio_stations.txt", "r") as f:
    for line in f:
        match = re.search(r"https?://([^:/\s]+)",line)
        if match:
            print(match.group(1))