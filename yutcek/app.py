#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Girilen anahtar kelimelerden youtube araması yaparak elde edilen sonuçları bir dosyaya işlemek için python dili ile gerçekleştirilmektedir.
import urllib2

main_url="http://gdata.youtube.com/feeds/api/videos?"
#Aramak istenilen anahtar kelime alınır
keyword = raw_input("Aranılacak metin?\n")
keyword= "+".join(keyword.split(" "))
#Toplam sonuç sayısı -düzenlenecek-
max_result=30
#Son url'yi belirle.
url=main_url+"q="+keyword+"&max-results="+str(max_result)+"&v=2"
#Verileri al
data = urllib2.urlopen(url).read()
#Dosya oluşturup veriyi gir.
dosya=open("file.txt","w")
#################veri içerisinden sadece başlık ve adresler çekilecek
dosya.write(data)
dosya.close()
