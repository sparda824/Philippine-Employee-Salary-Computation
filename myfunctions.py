# My separate Functions module.
# Did this to test how module importation works.

import sys
from decimal import *


def tax_computation(rate, terms, actual):
    global tardiness_deduction
    global taxable_income_true
    global witholding_tax
    rate_per_day = rate / 26
    rate_per_hour = rate_per_day / 8
    rate_per_min = rate_per_hour / 60
    print(
        '''
    How many absences do you have?
    --------------------------------------------
        ''')
    absent = int(input('Days: '))
    print(
        '''    --------------------------------------------
    How many minutes had you been late?
    --------------------------------------------
        ''')
    late = int(input('Minutes: '))
    absent_deduction = absent * rate_per_day
    late_deduction = late * rate_per_min
    tardiness_deduction = absent_deduction + late_deduction
    taxable_income = actual - tardiness_deduction
    taxable_income_true = Decimal(taxable_income).quantize(
        Decimal('.01'), rounding=ROUND_DOWN)
    if terms == 1:
        if taxable_income < 20833:
            witholding_tax = 0
        elif taxable_income >= 20833 and taxable_income < 33333:
            witholding_tax = int((taxable_income - 20833) * .2)
        elif taxable_income >= 33333 and taxable_income < 66667:
            witholding_tax = int(2500 + ((taxable_income - 33333) * .25))
        elif taxable_income >= 66667 and taxable_income < 166667:
            witholding_tax = int(10833.33 + ((taxable_income - 66667) * .3))
        elif taxable_income >= 166667 and taxable_income < 666667:
            witholding_tax = int(40833.33 + ((taxable_income - 166667) * .32))
        elif taxable_income >= 666667:
            witholding_tax = int(200833.33 + ((taxable_income - 666667) * .35))
        else:
            print('Encountered an unexpected error, Terminating')
            sys.exit()
    if terms == 2:
        if taxable_income < 10417:
            witholding_tax = 0
        elif taxable_income >= 10417 and taxable_income < 16667:
            witholding_tax = int((taxable_income - 10417) * .2)
        elif taxable_income >= 16667 and taxable_income < 33333:
            witholding_tax = int(1250 + ((taxable_income - 16667) * .25))
        elif taxable_income >= 33333 and taxable_income < 83333:
            witholding_tax = int(5416.67 + ((taxable_income - 33333) * .3))
        elif taxable_income >= 83333 and taxable_income < 333333:
            witholding_tax = int(20416.67 + ((taxable_income - 833333) * .32))
        elif taxable_income >= 333333:
            witholding_tax = int(100416.67 + ((taxable_income - 333333) * .35))
        else:
            print('Encountered an unexpected error, Terminating')
            sys.exit()


def sss_computation(rate, terms):
    global sss
    sss_bracket = 2250
    sss_contri = 80
    if rate > 19750:
        sss_contri = 800
    else:
        while sss_bracket <= rate:
            sss_bracket += 500
            sss_contri += 20
    sss = sss_contri / terms


def phil_computation(rate, terms):
    global phil
    if rate < 10000:
        phil = 137.5 / terms
    elif rate >= 10000.01 and rate < 39999.99:
        phil = (rate * .01375) / terms
    else:
        phil = 550 / terms


def hdmf_computation(rate, terms):
    global hdmf
    if rate > 5000:
        hdmf = 100 / terms
    elif rate < 5000 and rate > 1500:
        hdmf = rate * .02 / terms
    else:
        hdmf = (rate * .01) / terms
