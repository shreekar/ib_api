from enum import Enum


class Instrument(Enum):
    STK = 0
    BOND = 1
    EFP = 2
    FUT_EU = 3
    FUT_HK = 4
    FUT_NA = 5
    FUT_US = 6
    IND_EU = 7
    IND_HK = 8
    IND_US = 9
    PMONITOR = 10
    PMONITORM = 11
    SLB_US = 12
    STOCK_EU = 13
    STOCK_HK = 14
    STOCK_NA = 15
    WAR_EU = 16

    def __str__(self):
        return self.name.replace('_', '.')
