# Macbook Battery Rates
The battery drain on my new 16" Macbook Pro is pretty awful, so I wrote this Python script to calculate my battery drain rates.

Requirements:
 - [iStat Menus](https://bjango.com/mac/istatmenus/)
 - Python3 ([how to install](https://docs.python-guide.org/starting/install3/osx/))

This script reads iStat's battery history database and calculates your average and max battery drain rate (in percent per hour) for the last day, week, and month.

## Sample output
```
(%/hr)  Max   Average
Day     -48       -24
Week    -39       -19
Month   -31       -11
```
