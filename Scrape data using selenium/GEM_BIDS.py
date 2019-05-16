import _thread
import os
from selenium import webdriver
from time import sleep
import pandas
import datetime


folder=os.getcwd()
os.chdir(folder)
csv_file =os.listdir()
if('GEM_BID.csv' in csv_file):
    reader_csv=pandas.read_csv("GEM_BID.csv")
bids=[]
itemss=[]
quantitys=[]
addresss=[]
start_date_time=[]
end_date_time=[]
start_dates=[]
start_time=[]
end_time=[]
end_dates=[]
service_pdf_names=[]
folder=os.getcwd()
print(folder)
dir1=os.listdir()
if 'SERVICE BID' not in dir1:
    os.makedirs('SERVICE BID')
os.chdir(folder+'\\SERVICE BID')
files=os.listdir()
if files != []:
    files = [i.split("-")[-1].split(".")[0] for i in files]
path=os.getcwd()
os.chdir(folder)
url="https://bidplus.gem.gov.in/servicelists"
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {"download.default_directory":path})
browser = webdriver.Chrome(chrome_options=options)
browser.get(url)
last_page=browser.find_element_by_xpath('''//*[@id="pagination"]/ul/li/ul/li[6]/a''')
last_page.click()
page=browser.find_element_by_xpath('''//*[@id="pagination"]/ul/li/ul''')
num1=page.find_elements_by_class_name('active')[0].text
print(num1)
browser.quit()

def download_service_bid(first,last):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {"download.default_directory":path})
    browser = webdriver.Chrome(chrome_options=options)
    for y in range(first,last):
        url1="https://bidplus.gem.gov.in/servicelists?servicelists&page_no="+str(y)
        browser.get(url1)
        
        for i in range(1,11):
            path_bid='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[1]/p[1]/a'''
            try:
                bid_no=browser.find_element_by_xpath(path_bid)
                links=bid_no.get_attribute('href')               
                link_name = links.split("/")[-1]
                service_pdf_names.append(link_name)
            except Exception as e:
                print("[ERROR]: "+str(e))
                break
            if link_name not in files:
                bids.append(bid_no.text)
                
                path_items='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[2]/p[1]/span'''
                items=browser.find_element_by_xpath(path_items)
                itemss.append(items.text)
                
                path_quantity='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[2]/p[2]/span'''
                quantity=browser.find_element_by_xpath(path_quantity)
                quantitys.append(quantity.text)
                
                path_address='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[3]/p[2]'''
                address=browser.find_element_by_xpath(path_address)
                addresss.append(address.text)
                
                path_start_date='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[4]/p[1]/span'''
                start_date=browser.find_element_by_xpath(path_start_date)
                start_date_time.append(start_date.text)
                
                path_end_date='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[4]/p[2]/span'''
                end_date=browser.find_element_by_xpath(path_end_date)
                end_date_time.append(end_date.text)
                
                bid_no.click()
    sleep(10)
    browser.quit()   
    os.chdir(folder)
    
    browser.quit()

download_service_bid(1,int(num1))

url="https://bidplus.gem.gov.in/servicelists"
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {"download.default_directory":path})
browser = webdriver.Chrome(chrome_options=options)
browser.get(url)
last_page=browser.find_element_by_xpath('''//*[@id="pagination"]/ul/li/ul/li[6]/a''')
last_page.click()
page=browser.find_element_by_xpath('''//*[@id="pagination"]/ul/li/ul''')
num2=page.find_elements_by_class_name('active')[0].text
print(num2)
browser.quit()
if int(num2)>int(num1):
    download_service_bid(int(num1),int(num2))

os.chdir(folder+'\\SERVICE BID')
files1=os.listdir()
for i in range(0,len(files1)):
    os.rename(files1[i],files1[i].split("-")[-1])
os.chdir(folder)
for z in range(0,len(start_date_time)):
    start_dates.append(start_date_time[z][:10])
    start_time.append(start_date_time[z][10:])
    end_dates.append(end_date_time[z][:10])
    end_time.append(end_date_time[z][10:])


bidp=[]
itemp=[]
quantityp=[]
addressp=[]
start_datep_time=[]
end_datep_time=[]
start_datep=[]
end_datep=[]
start_timep=[]
end_timep=[]
service_pdf_namep=[]

folder=os.getcwd()
print(folder)
dir1=os.listdir()
if 'PRODUCT BID' not in dir1:
    os.makedirs('PRODUCT BID')
os.chdir(folder+'\\PRODUCT BID')
files2=os.listdir()
if files2 != []:
    files2 = [i.split("-")[-1].split(".")[0] for i in files2]
path=os.getcwd()
os.chdir(folder)
url="https://bidplus.gem.gov.in/bidlists"
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {"download.default_directory":path})
browser = webdriver.Chrome(chrome_options=options)
browser.get(url)
last_page=browser.find_element_by_xpath('''//*[@id="pagination"]/ul/li/ul/li[6]/a''')
last_page.click()

page=browser.find_element_by_xpath('''//*[@id="pagination"]/ul/li/ul''')
num1=page.find_elements_by_class_name('active')[0].text

print(num1)
browser.quit()
def download_product_bid(first,last):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {"download.default_directory":path})
    browser = webdriver.Chrome(chrome_options=options)
    for y in range(first,last):
        url1="https://bidplus.gem.gov.in/bidlists?bidlists&page_no="+str(y)
        browser.get(url1)
        for i in range(1,11):
            path_bid='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[1]/p[1]/a'''
            try:
                bid_no=browser.find_element_by_xpath(path_bid)
                links=bid_no.get_attribute('href')               
                link_name = links.split("/")[-1]
                service_pdf_namep.append(link_name)
            except Exception as e:
                print("[ERROR]: "+str(e))
                break
            if link_name not in files2:
                bidp.append(bid_no.text)
                
                path_items='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[2]/p[1]/span'''
                items=browser.find_element_by_xpath(path_items)
                itemp.append(items.text)
                
                path_quantity='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[2]/p[2]/span'''
                quantity=browser.find_element_by_xpath(path_quantity)
                quantityp.append(quantity.text)
                
                path_address='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[3]/p[2]'''
                address=browser.find_element_by_xpath(path_address)
                addressp.append(address.text)
                
                path_start_date='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[4]/p[1]/span'''
                start_date=browser.find_element_by_xpath(path_start_date)
                start_datep_time.append(start_date.text)
                
                path_end_date='''//*[@id="pagi_content"]/div['''+str(i)+''']/div[4]/p[2]/span'''
                end_date=browser.find_element_by_xpath(path_end_date)
                end_datep_time.append(end_date.text)
                
                bid_no.click()
    sleep(10)
    browser.quit()   
    os.chdir(folder)
div=int(int(num1)/100)
for i in range(1,div):
    _thread.start_new_thread(download_product_bid, (100*i,(i*100)+100, )) 

download_product_bid(1,100)
download_product_bid(div*100,int(num1))
sleep(40)

url="https://bidplus.gem.gov.in/bidlists"
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {"download.default_directory":path})
browser = webdriver.Chrome(chrome_options=options)
browser.get(url)
last_page=browser.find_element_by_xpath('''//*[@id="pagination"]/ul/li/ul/li[6]/a''')
last_page.click()

page=browser.find_element_by_xpath('''//*[@id="pagination"]/ul/li/ul''')
num2=page.find_elements_by_class_name('active')[0].text

print(num2)
browser.quit()
if int(num2)>int(num1):
    download_product_bid(int(num1),int(num2))


os.chdir(folder+'\\PRODUCT BID')
files3=os.listdir()
for i in range(0,len(files3)):
    try:
        os.rename(files3[i],files3[i].split("-")[-1])
    except Exception as e:
        print("[ERROR]: "+str(e))
                    
os.chdir(folder)

for z in range(0,len(start_datep_time)):
    start_datep.append(start_datep_time[z][:10])
    start_timep.append(start_datep_time[z][10:])
    end_datep.append(end_datep_time[z][:10])
    end_timep.append(end_datep_time[z][10:])

type1=[]
BID_No=[]
Items=[]
Quantity_Required=[]
Department_Name_And_Address=[]
Start_Date=[]
Start_Time=[]
End_Date=[]
End_Time=[]
Pdf_Name=[]
#
#
#compairsion_list = [i.split(".")[0] for i in list(reader_csv['PDF NAME'])]
#
#
#    
#    if link_s.split(".")[0] not in compairsion_list and link_p.split(".")[0] not in compairsion_list:
for i in range(0,len(bids)):
    Pdf_Name.append(service_pdf_names[i])
    type1.append("SERVICE")
    BID_No.append(bids[i])
    Items.append(itemss[i])
    Quantity_Required.append(quantitys[i])
    Department_Name_And_Address.append(addresss[i])
    Start_Date.append(start_dates[i])
    Start_Time.append(start_time[i])
    End_Date.append(end_dates[i])
    End_Time.append(end_time[i])
for i in range(0,len(bidp)):
    Pdf_Name.append(service_pdf_namep[i])
    type1.append("PRODUCT")
    BID_No.append(bidp[i])
    Items.append(itemp[i])
    Quantity_Required.append(quantityp[i])
    Department_Name_And_Address.append(addressp[i])
    Start_Date.append(start_datep[i])
    Start_Time.append(start_timep[i])
    End_Date.append(end_datep[i]) 
    End_Time.append(end_timep[i])
   
    

make_csv=pandas.DataFrame()
make_csv["Type"]=type1
make_csv["RA/BID NO."]=BID_No
make_csv["Items"]=Items
make_csv["Quantity Required"]=Quantity_Required
make_csv["Department Name And Address"]=Department_Name_And_Address
make_csv["Start Date"]=Start_Date
make_csv["Start Time"]=Start_Time
make_csv["End Date"]=End_Date
make_csv["End Time"]=End_Time
make_csv["PDF NAME"]=[Pdf_Name[i].split("/")[-1]+'.pdf' for i in range(0,len(Pdf_Name))]

df2=pandas.concat([reader_csv,make_csv],ignore_index=True)
df2.to_csv("GEM_BID.csv",index=False)
t=datetime.datetime.now()
name=str(t)[0:13]+".csv"
make_csv.to_csv(name)





