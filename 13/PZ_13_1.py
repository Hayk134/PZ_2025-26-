'''
В исходном текстовом файле (radio stations.txt) найти все домены из URL-адресов
(HanpиMep, B URL-a pece http://stream.hoster.by:8081/pilotfn/audio/icecast.audio домен
выделен полужирным).
'''

with open("radio_stations.txt", "r") as f:

    domains = (
        line[line.find("http"):].strip().split("//")[1].split("/")[0].split(":")[0]
        for line in f
        if "http" in line
    )


    for d in domains:
        print(d)