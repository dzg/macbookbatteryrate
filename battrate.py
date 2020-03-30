import os, sqlite3
hour = 3600
scopes = ['day', 'week', 'month']
shellcmd = "ioreg -rd1 -c AppleSmartBattery | awk -F\\\" '/BatterySerialNumber/ { print $(NF-1) }'"
battserial = os.popen(shellcmd).read().splitlines()[0]
dbpath = os.path.expanduser('~') + '/Library/Application Support/iStat Menus/databases/iStatMenusStatus.db'
c = sqlite3.connect(dbpath).cursor()

print('(%/hr)  Max   Average')
for scope in scopes:
    c.execute('SELECT time,percentage from {}_batteryhistory where uuid="{}"'.format(scope, battserial))
    data = c.fetchall()
    rates = []
    for row in range(0, len(data) - 1):
        t = data[row + 1][0] - data[row][0]
        p = data[row + 1][1] - data[row][1]
        rates.append(p / (t / hour))
    neg = list(filter(lambda x: x < 0, rates))
    print("{:5} {:5.0f} {:9.0f}".format(scope.capitalize(), min(rates), sum(neg) / len(neg)))
