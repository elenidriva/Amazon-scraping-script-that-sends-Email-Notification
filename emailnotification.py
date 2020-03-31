import smtplib
import sys 
import time

from bs4 import  BeautifulSoup
import requests

def checkIfLegitInput(URL_str):
    URL_list = URL_str.split(',')
    print(URL_list)  
    len(URL_list)
    counter = 0
    for eachURL in URL_list:
        if eachURL.find('https://www.amazon.com/')!= -1:
            counter = counter + 1
            continue
        else:
            print("The URL: "+ eachURL+"found in position "+ str(counter)+" is invalid")
            print("Please re-enter the AMAZON URLs of products correctly this time.")
            URL_list = []
            break
    return URL_list

def parseData(URL_list):
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36' }
    
    '''wb = xlwt.Workbook()
    sheet = wb.add_sheet("Price Tracking Sheet")
    row_counter = 1
    sheet.write(0,0, "Product")
    sheet.write(0,1,"Price")
    for each_URL in URL_list:
        sub_page = requests.get(each_URL, headers=headers)
        parser_page = BeautifulSoup(sub_page.content, 'html.parser')
        title = parser_page.find('h1', class_='page-title').text.strip() # div class="description anchor--no-style"
        price = parser_page.find('span', class_='ultra-bold test-price-property').text.strip()
        #print(title)
        #print(price)
        sheet.write(row_counter,0,title)
        sheet.write(row_counter,1,price)
        row_counter = row_counter + 1
    wb.save('Products and Prices.xls')    '''
    titles_list = []
    prices_list = []
    for each_URL in URL_list:
        sub_page = requests.get(each_URL, headers=headers)
        parser = BeautifulSoup(sub_page.content, 'html5lib')
        #print(parser)
        title = parser.find(id="productTitle").text.strip()
        price = parser.find('span', class_="a-size-base a-color-price header-price a-text-normal").text
        titles_list.append(title)
        prices_list.append(price.replace('$',''))
    print(titles_list)
    print(prices_list)
    return titles_list, prices_list
    
def comparePrices(titles_list, prices_list, URL_list):
    prices_31_03 = ['84.99', '147.99', '87.99']
    i=0
    while i < len(prices_31_03):
        if prices_31_03[i] > prices_list[i]:
           print("Sending email to inform about the price drop.")
           sendEmail(titles_list[i], prices_list[i], prices_31_03[i], URL_list[i])
        i = i + 1

    
def sendEmail(product, current_price, previous_price, URL):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() #establishes connection 
    server.starttls() #encrypts connection
    server.ehlo()
    server.login('elenidriva96@gmail.com', 'flywqnhyptgzzklh')     
    subject = " Price of " + product + " fell down!"
    body = "The product " + product + " now costs " + current_price + " $ " + "down from " + previous_price + " $\nGo check it out here: " + URL
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('elenidriva96@gmail.com',
                    'elenidriva96@gmail.com',
                    msg)
    print("Email has been sent!")
    server.quit()
    

URL_str = 'https://www.amazon.com/dp/B0781Z7Y3S/ref=psdc_1292116011_t1_B00E3W1726, https://www.amazon.com/Samsung-512GB-V-NAND-Solid-MZ-76P512BW/dp/B07836C6YV?ref_=s9_apbd_simh_hd_bw_b1PRaOp&pf_rd_r=0SX9J6G87ZCPTN9BW7HD&pf_rd_p=5e982072-3675-5d4b-98b7-9d016bdf5c5c&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=1292116011, https://www.amazon.com/Samsung-512GB-V-NAND-Solid-MZ-76P512BW/dp/B07864XMTK?ref_=s9_apbd_simh_hd_bw_b1PRaOp&pf_rd_r=0SX9J6G87ZCPTN9BW7HD&pf_rd_p=5e982072-3675-5d4b-98b7-9d016bdf5c5c&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=1292116011&th=1'
URL_list = checkIfLegitInput(URL_str)
print("All URLs are correct.\n")
titles_list, prices_list = parseData(URL_list)   
#while(True):
comparePrices(titles_list, prices_list, URL_list) 
    #time.sleep(1800)
'''
i = 1
URL_str = ""
while i < len(sys.argv):
    URL_str = URL_str +','+ sys.argv[i] 
    i = i + 1
URL_str = URL_str.replace(',', '', 1)  
#URL_str = input("Please copy and paste the URL of a specific product or if you want to add a list of products insert multiple URLS divided by ','(comma)\n")
URL_list = checkIfLegitInput(URL_str)
while len(URL_list) == 0:
    URL_str = input("Please copy and paste the URL of a specific product or if you want to add a list of products insert multiple URLS divided by ','(comma)\n")
    URL_list = checkIfLegitInput(URL_str)
print("All URLs are correct.\n")
print(URL_list)
titles_list, prices_list = parseData(URL_list)   
while(True):
    comparePrices(titles_list, prices_list, URL_list) 
    time.sleep(1800)


URL = "https://www.amazon.com/dp/B0781Z7Y3S/ref=psdc_1292116011_t1_B00E3W1726"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36' }

page = requests.get(URL, headers=headers)
parser = BeautifulSoup(page.content, 'html.parser')
title = parser.find(id="productTitle").text
price = parser.find(id="buyNew_noncbb").text
# tis times se lista olwn twn url gia polla allaaaa
#print(title)
#print(float(price.replace('$', '')))
if float(price.replace('$', '')) != 70.39:
    #print(float(price.replace('$', '')))
    send_mail()
'''