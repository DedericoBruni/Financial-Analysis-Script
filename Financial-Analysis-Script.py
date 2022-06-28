import Bruni.Pstd as brn
from pyfiglet import Figlet
import sys, time, threading
from os import system, name


def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def the_process_function(alloc):
    k = brn.find_best_allocation(tickers,year,month,day,iterations)
    for i in range(len(k)):
        alloc.append(k[i])

def animated_loading():
    chars = "/—\|" 
    for char in chars:
        sys.stdout.write('\r'+'loading...'+char)
        time.sleep(.1)
        sys.stdout.flush() 

check = 'y'
while check == 'y':
    f = Figlet(font='slant')
    print(f.renderText('Portfolio Analysis'))
    print('By Federico Bruni')
    print()
    print('Choose an Operation: ')
    print('1- Portfolio Standard Deviation')
    print('2- Portfolio Expected Return')
    print('3- Portfolio Correlation')
    print('4- Find Best Allocation')
    print('5- Compound Annual Growth Rate')
    print()
    choice = input('')
    check = True
    w = []
    tickers = []

    if choice == '1':
        N = int(input('Insert The Number Of Stocks: '))
        capital = int(input('Insert total capital invested: '))
        i = 0
        while i < N:
            ticker = input('Insert Ticker: ').upper()
            investment = int(input('Investment on the stock(integer): '))
            tickers.append(ticker)
            weight = investment/capital
            w.append(weight)
            i += 1
        
        print()
        year = int(input('Insert Starting Year: '))
        month = int(input('Insert Starting Month: '))
        day = int(input('Insert Starting Day: '))
        std = brn.portfolio_std(tickers,w,year,month,day)
        std = round(std*100,4)
        print()
        print(std, '%')
        time.sleep(2)
    
    if choice == '2':
        N = int(input('Insert The Number Of Stocks: '))
        capital = int(input('Insert total capital invested: '))
        i = 0
        while i < N:
            ticker = input('Insert Ticker: ').upper()
            investment = int(input('Investment on the stock(integer): '))
            tickers.append(ticker)
            weight = investment/capital
            w.append(weight)
            i += 1
        
        print()
        year = int(input('Insert Starting Year: '))
        month = int(input('Insert Starting Month: '))
        day = int(input('Insert Starting Day: '))
        ret = brn.portfolio_return(tickers,w,year,month,day)
        ret = (1+ret)**252 -1
        ret = round(ret,2)
        print()
        print(ret, '% Annualized Expected Return')
        time.sleep(2)


    if choice == '3':
        N = int(input('Insert The Number Of Stocks: '))
        i = 0
        while i < N:
            ticker = input('Insert Ticker: ').upper()
            tickers.append(ticker)
            i += 1
        
        print()
        year = int(input('Insert Starting Year: '))
        month = int(input('Insert Starting Month: '))
        day = int(input('Insert Starting Day: '))
        corr = brn.portfolio_corr(tickers,year,month,day)
        print()
        print(corr)
        print()
        corr['Mean']=(corr.sum()-1)/(N-1)
        mean_corr = corr['Mean'].mean() 
        print(' Mean Correlation is:',mean_corr)
        time.sleep(2)


    if choice == '4':
        N = int(input('Insert The Number Of Stocks: '))
        i = 0
        while i < N:
            ticker = input('Insert Ticker: ').upper()
            tickers.append(ticker)
            i += 1
        
        print()
        year = int(input('Insert Starting Year: '))
        month = int(input('Insert Starting Month: '))
        day = int(input('Insert Starting Day: '))
        iterations = int(input('Number of iterations for Montecarlo Simulation: '))
        alloc = []
        the_process = threading.Thread(name='process', target=the_process_function,args=(alloc,))
        the_process.daemon = True
        the_process.start()
        while the_process.is_alive():
            animated_loading()
        i = 0
        for i in range(len(alloc)):
            alloc[i] = round(alloc[i],3)
        print()
        print('Best allocations: ', alloc)
        print()
        time.sleep(2)
        

    if choice == '5':
        import datetime as dt
        import pandas_datareader as pdr
        ticker = input('Insert Ticker: ').upper()
        print()
        Ys = int(input('Insert Starting Year: '))
        Ms = int(input('Insert Starting Month: '))
        Ds = int(input('Insert Starting Day: '))
        print()
        Yf = input('Insert Ending Year: ')
        Mf = input('Insert Ending Month: ')
        Df = input('Insert Ending Day: ')
        Ys = int(Ys)
        Ms = int(Ms)
        Ds = int(Ds)
        start = dt.datetime(Ys, Ms, Ds)
        df = pdr.get_data_yahoo(ticker, start)
        price_s = float(df.iloc[0]['Close'])
        price_f = float(df.loc[Yf+'-'+Mf+'-'+Df]['Close'])
        df = df.loc[:Yf+'-'+Mf+'-'+Df]
        t = float(len(df)/365)
        cagr = (price_f / price_s)**(1 / t) - 1
        cagr = round(cagr*100,2)
        cagr = str(cagr)
        cagr = cagr+'%'
        print('CAGR: '+cagr)
        print()
        time.sleep(2)


    check = input('Want to restart?(y/n) ')
    if check == 'y':
        clear()
