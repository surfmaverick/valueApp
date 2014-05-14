__author__ = 'Christopher L Smith'import pandas as pdfrom datetime import datetimeimport numpy as npfrom dateutil.relativedelta import relativedeltadef preparedates(startdate, enddate, freq='M'):    """    prepareDates produces a series of dates with an irregular commencement date and an irregular end date.    """    dates = []    dates.append(pd.index.Timestamp(startdate))    currentdate = startdate    if freq == 'M':        roll = True        while roll:            nextdate = pd.tseries.offsets.MonthEnd() + currentdate            if nextdate > enddate:                roll = False                dates.append(pd.index.Timestamp(enddate))                break            else:                dates.append(nextdate)                currentdate = nextdate + pd.tseries.offsets.DateOffset(days=1)    # a different method was used for quarter end because pandas does not hvae a "Quarter" for DateOffset.    # pandas actually refers to relativedate, which is used here    # TODO:  modify dates accordingly so that we have a unified "date" engine--maybe build own date engine    # working off of scikit?    if freq == 'Q':        offset = pd.tseries.offsets.QuarterEnd()        roll = True        while roll:            nextdate = offset + currentdate            if nextdate > enddate:                roll = False                dates.append(pd.index.Timestamp(enddate))                break            else:                dates.append(nextdate)                currentdate = nextdate + relativedelta(days=1)    return datesdef monthlytoquarterly(monthlies,firstquarterendingmonth=3):    results = {1:0,2:0,3:0,4:0}    for g,v in monthlies.items():        if (g < 1 + firstquarterendingmonth) and (g > 0 + firstquarterendingmonth - 3):            results[1] = results[1] + v        if (g < 4 + firstquarterendingmonth) and (g > 3 + firstquarterendingmonth - 3):            results[2] = results[2] + v        if (g < 7 + firstquarterendingmonth) and (g > 6 + firstquarterendingmonth - 3):            results[3] = results[3] + v        if (g < 10 + firstquarterendingmonth) and (g > 9 + firstquarterendingmonth - 3):            results[4] = results[4] + v    return resultsclass PowerPlant():    """    This is an operating asset that has numerous proporties that define it, including whether it is operating or under    construction, what kind of asset it is, etc.    The program logic is to create facilities that have different properties.  Each property will have its own costs,    dates and application rules referred to as an 'application methods'.  The anticipated macro properties are:        construction schedules        production schedules        revenue schedules        expense schedules        maintenance schedules    These combined will produce a series of operatng cash flows.    An 'application method' can be either fixed, calendar, or volumetrically applied.  Application methods can    include cut in dates, cut out dates, or blackout dates.    Then, a "facility" will be rolled up into a portfolio to be combined together into a series of    cash flows that will be evaluated under a set of financing rules.    """    def __init__(self, name, type=None, description=None,location=None, latitude=None, longitude=None, dates=None, periods='M'):        """        Initializes a power plant asset for valuation purposes.        """        self.info = {}        self.name = name        self.info['name'] = name        self.info['type'] = type        self.info['description'] = description        self.info['location'] = location        self.info['latitude'] = latitude        self.info['longitude'] = longitude        self.info['periods'] = periods    def setup_frame(self, dates, dfname):        setattr(self, dfname, pd.DataFrame(index=dates))        x = getattr(self, dfname)        x['date'] = x.index        x['timespan'] = x['date'] - x['date'].shift(1)        x['elapsed_time'] = x['date'] - x['date'].iloc[0]    def setup_production_schedule(self, prodschedule, dfname='ops', dfcolumn='production'):        #first get the object DataFrame we want to work on        x = getattr(self, dfname)        if self.info['periods'] == 'M':            forward = pd.tseries.offsets.MonthEnd()            back = pd.tseries.offsets.MonthBegin()            period = 'month'        elif self.info['periods']  == 'Q':            forward = pd.tseries.offsets.QuarterEnd(startingMonth=3)            back = pd.tseries.offsets.QuarterBegin(startingMonth=1)            period = 'quarter'        # then get the column we want to utilize. If it errors then the column probably hasn't been created yet.        try:            getattr(x, dfcolumn)        # failed, so create the column        except:            x[dfcolumn] = None        # proceed down the index        for row in x.index:            #get the column we want to actually work on            y = getattr(x, dfcolumn)            z = getattr(x,'timespan')            #now we calculate the percentage of the period (or "timespan" we are actually operating            #total days in the timespan            maximum = (forward.rollforward(row) - back.rollback(row)).days+1            # percentage of period            try:                percentage = ((z[row] / np.timedelta64(1, 'D')) / maximum)            except:                percentage = 0            #actual time span            y[row] = prodschedule[getattr(row,period)] * percentage    def _setup_escalation(self):        passclass WindPowerPlant(PowerPlant):    def __init__(self, name, type=None, periods='M'):        PowerPlant.__init__(self, name, type=type, periods=periods)class BiomassPowerPlant(PowerPlant):    passclass NuclearPowerPlant(PowerPlant):    passclass CoalPowerPlant(PowerPlant):    pass