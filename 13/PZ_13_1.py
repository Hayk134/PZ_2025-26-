'''
В исходном текстовом файле (radio stations.txt) найти все домены из URL-адресов
(HanpиMep, B URL-a pece http://stream.hoster.by:8081/pilotfn/audio/icecast.audio домен
выделен полужирным).
'''

f = open("radio_stations.txt", "r")
for line in f:
    if "http" in line:
        url = line[line.find("http"):].strip()
        parts = url.split("//")[1]
        domain_port = parts.split("/")[0]
        domain = domain_port.split(":")[0]
        print(domain)
f.close()