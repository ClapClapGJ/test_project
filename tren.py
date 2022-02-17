import datetime
import random

payload = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" " \
          "xmlns:ser=\"http://service.callcenter.ems.ru/\"><soapenv:Header/><soapenv:Body>" \
          "<ser:saveOrders><!--Optional:--> <apikey>1234</apikey> <!--Zero or " \
          "more repetitions:--><order><!--Optional:-->" \
          "<orderNumber>PP22011970</orderNumber><!--Optional:-->" \
          f"<createdDate>2022-01-17</createdDate> <!--Optional:-->" \
          "<changedBy>4125</changedBy><!--Optional:-->" \
          f"<changedDate></changedDate><!--Optional:-->" \
          f"<status>1</status><!--Optional:--><orderDate>2022-01-17</orderDate>" \
          "<!--Optional:--><orderTime>4</orderTime><!--Optional:--> " \
          "<orderType>4</orderType><orderOSP>130201</orderOSP>" \
          "<!--Optional:--><orderRegion>6</orderRegion><!--Optional:-->" \
          "<printDocument>0</printDocument><orderRoute>33063</orderRoute>" \
          "<!--Optional:--><fullAddress>, Российская федерация, Москва г,   Хорошевское ш, 33, "\
          "1</fullAddress><!--Optional:--><street>?</street>" \
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
now = datetime.datetime.now()
ran = random.randrange(60000, 80000)
print(ran)
