# This is my first Programming project as an aspiring programmer.
# In case you found something that can be written better please let me know asap.
# I am an accountant that is why this is my chosen project.
# I'm a self thought programmer so please be patient if there are many errors.

import sys
import myfunctions as mf
from decimal import *

print(
    '''    Hi, My name is:
    --------------------------------------------
     ____       
    |          *     |
    |____   __    __ | __  __  ___    __
    |     |/   | |   |/   |__ |   | |/  |
    |____ |    | |__ |\\__  __||___| |   |
    --------------------------------------------
    Please type your name to begin.
    --------------------------------------------
    '''
)
users_name = str(input('Name: '))
print(
    '''    --------------------------------------------
    Welcome to my Tax/SSS Computation Program
    --------------------------------------------
    ''')


def main():
    print(
        f'''    --------------------------------------------
    Mr.{users_name}
    Please indicate your Salary Rate
    --------------------------------------------
        '''
    )
    try:
        rate = int(input('Rate: '))
        print(
            f'''    --------------------------------------------        
    I see, so your earning {rate} per month
    May I know how are you being paid?
    Is it monthly or semi-monthly?
    (please type in lower case)
    --------------------------------------------
        '''
        )
    except ValueError:
        print('Invalid Response, Please try again later')
        sys.exit()
    try_1 = 1
    while try_1 < 4:
        global terms
        terms = (input('terms: ')).lower()
        if terms == 'monthly':
            terms = 1
            print(
                '''    --------------------------------------------        
    Ok, so you are being paid in full.
                '''
            )
            actual_rate = rate
            mf.tax_computation(rate, terms, actual_rate)
            mf.sss_computation(rate, terms)
            mf.phil_computation(rate, terms)
            mf.hdmf_computation(rate, terms)
            tardiness = Decimal(mf.tardiness_deduction).quantize(
                Decimal('.01'), rounding=ROUND_DOWN)
            witholding_tax = Decimal(mf.witholding_tax).quantize(
                Decimal('.01'), rounding=ROUND_DOWN)
            sss = Decimal(mf.sss).quantize(Decimal('.01'), rounding=ROUND_DOWN)
            phil = Decimal(mf.phil).quantize(
                Decimal('.01'), rounding=ROUND_DOWN)
            hdmf = Decimal(mf.hdmf).quantize(
                Decimal('.01'), rounding=ROUND_DOWN)
            netpay = Decimal(mf.taxable_income_true - witholding_tax - sss -
                             phil - hdmf).quantize(Decimal('.01'), rounding=ROUND_DOWN)
            print(
                f'''    --------------------------------------------    
    Income:             {rate}
    Tardiness:          {tardiness}
    --------------------------------------------
    Gross Pay:              {rate - tardiness}    
    --------------------------------------------
    Less Deductions:
        Witholding Tax: {witholding_tax}
        SSS:            {sss}
        Philhealth:     {phil}
        Pagibig:        {hdmf}
    Total Deductions:       {witholding_tax + sss + phil + hdmf}
    --------------------------------------------
    Net Pay:                {netpay}
    --------------------------------------------
            ''')
            print('Would you like to make another inquiry?')
            another = input('Another?:').lower()
            if another in ['yes', 'y', 'ye']:
                main()
            else:
                print(f'Goodbye {users_name}')
                sys.exit()
        elif terms == 'semi-monthly':
            terms = 2
            print(
                f'''    --------------------------------------------
    Ok, so you are being paid {rate/2} per payout.
                '''
            )
            actual_rate = rate / 2
            mf.tax_computation(rate, terms, actual_rate)
            mf.sss_computation(rate, terms)
            mf.phil_computation(rate, terms)
            mf.hdmf_computation(rate, terms)
            tardiness = Decimal(mf.tardiness_deduction).quantize(
                Decimal('.01'), rounding=ROUND_DOWN)
            witholding_tax = Decimal(mf.witholding_tax).quantize(
                Decimal('.01'), rounding=ROUND_DOWN)
            sss = Decimal(mf.sss).quantize(Decimal('.01'), rounding=ROUND_DOWN)
            phil = Decimal(mf.phil).quantize(
                Decimal('.01'), rounding=ROUND_DOWN)
            hdmf = Decimal(mf.hdmf).quantize(
                Decimal('.01'), rounding=ROUND_DOWN)
            netpay = Decimal(mf.taxable_income_true - witholding_tax - sss -
                             phil - hdmf).quantize(Decimal('.01'), rounding=ROUND_DOWN)
            print(
                f'''    --------------------------------------------    
    Income:             {rate}
    Tardiness:          {tardiness}
    --------------------------------------------
    Gross Pay:              {rate - tardiness}   
    -------------------------------------------- 
    Less Deductions:
        Witholding Tax: {witholding_tax}
        SSS:            {sss}
        Philhealth:     {phil}
        Pagibig:        {hdmf}
    Total Deductions:       {witholding_tax + sss + phil + hdmf}
    --------------------------------------------
    Net Pay:                {netpay}
    --------------------------------------------
            ''')
            print('Would you like to make another inquiry?')
            another = input('Another?:').lower()
            if another in ['yes', 'y', 'ye']:
                main()
            else:
                print(f'Goodbye {users_name}')
                sys.exit()
        else:
            print('Please indicate the exact word')
            try_1 += 1
    else:
        print('Please reopen program as soon as you can answer, Thank you')
        sys.exit


main()
