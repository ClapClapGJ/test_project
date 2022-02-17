import datetime
import random
import requests
import threading
import time

url = "http://judy/gt-ws/OrderSaveService"
now = datetime.datetime.now()
date = now.isoformat()
order_num = random.randrange(60000, 80000)


def newsbor():
    order_num = random.randrange(60000, 80000)
    payload = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" " \
              "xmlns:ser=\"http://service.callcenter.ems.ru/\"><soapenv:Header/><soapenv:Body>" \
              "<ser:saveOrders><!--Optional:--> <apikey>1234</apikey> <!--Zero or " \
              "more repetitions:--><order><!--Optional:-->" \
              f"<orderNumber>{order_num}</orderNumber><!--Optional:-->" \
              f"<createdDate>{date}</createdDate> <!--Optional:-->" \
              "<changedBy>4125</changedBy><!--Optional:-->" \
              f"<changedDate>{date}</changedDate><!--Optional:-->" \
              f"<status>1</status><!--Optional:--><orderDate>{date}</orderDate>" \
              "<!--Optional:--><orderTime>4</orderTime><!--Optional:--> " \
              "<orderType>4</orderType><orderOSP>130201</orderOSP>" \
              "<!--Optional:--><orderRegion>6</orderRegion><!--Optional:-->" \
              "<printDocument>0</printDocument><orderRoute>33063</orderRoute>" \
              "<!--Optional:--><fullAddress>117535 Москва Москва Россошанская 3 к2"\
              "</fullAddress><!--Optional:--><street>?</street>" \
              "<!--Optional:--><house>?</house><!--Optional:-->" \
              "<building>?</building><!--Optional:--><entrance>?</entrance>" \
              "<!--Optional:--><intercom>?</intercom><!--Optional:-->" \
              "<floor>?</floor><!--Optional:--><objectType>?</objectType>" \
              "<!--Optional:--><apartmentNumber>?</apartmentNumber><!--Optional:--> " \
              "<officeNumber>?</officeNumber><!--Optional:-->" \
              "<locationProperties>?</locationProperties><!--Optional:-->" \
              "<contactName>Райская Лилия Викторовна, Цыганкова Юлия Михайловна</contactName>" \
              "<!--Optional:--><senderName>?</senderName><!--Optional:-->" \
              "<clientName>ООО «СОБСТВЕННАЯ ТОРГОВАЯ МАРКА»</clientName><!--Optional:-->" \
              "<contractNumber>7734135</contractNumber><!--Optional:-->" \
              "<phone>8-926-069-21-22, 8-925-411-52-03,</phone><!--Optional:-->" \
              "<internalPhone>?</internalPhone><!--Optional:--><places>?</places>" \
              "<!--Optional:--><parcelType>3</parcelType><!--Optional:--> " \
              "<parcelDescription></parcelDescription>  /----сюда имя доставки, которая будет привязана к " \
              "заказу<!--Optional:--><insurance>?</insurance>" \
              "<!--Optional:--><weight>12</weight><!--Optional:-->" \
              "<dimensions>?</dimensions><!--Optional:--><paymentType>4</paymentType> " \
              "<!--Optional:--><destinationCountry>1</destinationCountry>" \
              "<!--Optional:--><destinationRegion>?</destinationRegion>" \
              "<!--Optional:--><destinationCity>?</destinationCity><!--Optional:--> " \
              "<mailType></mailType><!--Optional:-->" \
              "<operatorComment>Отправление «Бизнес курьер»null;br/null;курьеру иметь при себе паспорт</operatorComment> " \
              "<!--Optional:--><dispatcherComment>?</dispatcherComment>" \
              "<!--Optional:--><orderComment>Подъезд 1 этаж 2, позвонить </orderComment>" \
              "<!--Optional:--><courierNeedPass>1</courierNeedPass><!--Optional:--> " \
              "<vehicleNeedPass>1</vehicleNeedPass><!--Optional:-->" \
              "<packaging>?</packaging><!--Optional:--><reasonDetail>32</reasonDetail> " \
              "<!--Optional:--><parcelQty>?</parcelQty>" \
              "<deliveryType>5</deliveryType></order></ser:saveOrders></soapenv:Body> " \
              "</soapenv:Envelope> "

    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                    ' Chrome/90.0.4430.93 Safari/537.36',
      'X-Requested-With': 'XMLHttpRequest',
      'Content-Type': 'text/xml',
      'Accept': '*/*',
      'Cookie': 'APPLICATION_SESS=950E78AC2576811CE7BA52E23E53735E; APP_SESS=130201; '
                'JSESSIONID=950E78AC2576811CE7BA52E23E53735E'
    }
    response = requests.post(url, headers=headers, data=payload.encode('utf-8'))
    print(response.status_code)
    print(response.text)
    print(order_num)


for t in range(10):
    threading.Thread(target=newsbor()).start()
time.sleep(2)


