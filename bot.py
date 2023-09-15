# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 01:15:52 2021

@author: habi cahya kumara
"""

from flask import Flask, request, redirect, url_for
from twilio.twiml.messaging_response import MessagingResponse
import re
import pandas as pd

app = Flask(__name__)

@app.route('/bot', methods=['POST']) 
def bot():    
    incoming_msg = request.values.get('Body', '').lower()
    str(incoming_msg)
    #print(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()   
    responded = False 
    df = pd.read_csv('https://raw.githubusercontent.com/habicahya/habicahya/main/DATA1.csv')    
    df['Subulussalam'] = df['Subulussalam'].str.lower()
    df['Aceh'] = df['Aceh'].str.lower()
    df['Indonesia'] = df['Indonesia'].str.lower() 
          
    all_var = df['Subulussalam'].unique().tolist()

    
    if 'menu' in incoming_msg or 'Mulai' in incoming_msg or 'Menu' in incoming_msg or 'Hallo' in incoming_msg or 'Hai' in incoming_msg or 'Halo' in incoming_msg: 
        text = menu()
        msg.body(text)
        responded = True
        
    elif 'm1' in incoming_msg:
        # return total cases
        text = brs()
        msg.body(text)
        responded = True
        
    elif 'BRS7' in incoming_msg or 'Brs7' in incoming_msg or 'brs7' in incoming_msg:    
        text = '📉 *Berita Resmi Statistik*\n*_Indeks Harga Konsumen/Inflasi Provinsi Aceh Februari 2021_* 📰\n\nPerkembangan harga berbagai komoditas pada Februari 2021 secara umum menunjukkan adanya penurunan. Pada Februari 2021 terjadi deflasi sebesar 0,65 persen, atau terjadi penurunan Indeks Harga Konsumen (IHK) dari 107,38 pada Januari 2021 menjadi 106,68 pada Februari 2021.Deflasi yang terjadi di Aceh (Gabungan 3 Kota) terjadi karena adanya penurunan harga yang ditunjukkan oleh turunnya indeks kelompok pengeluaran, yaitu: kelompok makanan, minuman dan tembakau sebesar 2,19 persen; kelompok perlengkapan, peralatan dan pemeliharaan rutin rumah tangga sebesar 0,31 persen; dan kelompok perawatan pribadi dan jasa lainnya sebesar 0,79 persen. Kelompok pengeluaran yang mengalami inflasi, yaitu: kelompok pakaian dan alas kaki sebesar 0,33 persen; kelompok perumahan, air, listrik, gas dan bahan bakar rumah tangga sebesar 0,30 persen; kelompok kesehatan sebesar 0,63 persen; kelompok transportasi sebesar 0,04 persen; kelompok informasi, komunikasi, dan jasa keuangan sebesar 0,18 persen; kelompok rekreasi, olahraga, dan budaya sebesar 0,03 persen; kelompok pendidikan sebesar 0,12 persen; dan kelompok penyediaan makanan dan minuman/restoran sebesar 0,01 persen. Tingkat inflasi tahun kalender (Januari–Februari) 2021 sebesar 0,13 persen dan tingkat inflasi tahun ke tahun (Februari 2021 terhadap Februari 2020) sebesar 2,59 persen. \n\nUntuk mendapatkan rilis resmi *BRS* ini 📰 silahkan download file dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/BRS_7.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/BRS_1.jpg')
        responded = True
    
    elif 'BRS6' in incoming_msg or 'Brs6' in incoming_msg or 'brs6' in incoming_msg:    
        text = '📉 *Berita Resmi Statistik*\n*_Perkembangan Transportasi dan Pariwisata Provinsi Aceh Januari 2021_* 📰\n\nPada bulan Januari 2021 jumlah penumpang yang tercatat di bandar udara  Iskandar Muda mencapai 25.481 orang, atau mengalami penurunan sebesar 29,59 persen jika dibandingkan dengan bulan Desember 2020. Secara total di Provinsi Aceh, jumlah penumpang pada bulan Januari 2021 mencapai 27.262 orang, mengalami penurunan dibandingkan bulan Desember 2020 sebesar 30,11 persen. Pada bulan Januari 2021 terdapat 474 penerbangan dalam negeri di 7 bandara dalam Provinsi Aceh. Belum ada penerbangan luar negeri disebabkan pandemi Covid – 19. Jumlah penumpang angkutan laut terbanyak pada bulan Januari 2021 terdapat pada pelabuhan Ulee Lheue yaitu tercatat sebanyak 72.881 penumpang, mengalami penurunan sebesar 8,93 persen terhadap bulan Desember 2020, juga terjadi penurunan sebesar 21,54 persen jika dibandingkan dengan bulan Januari 2020. Secara total di Provinsi Aceh, jumlah penumpang pada bulan Januari 2021 hanya mencapai 107.306 orang, mengalami penurunan sebesar 33,29 persen dibandingkan bulan Desember 2020, namun mengalami penurunan sebesar 44,28 persen dibandingkan bulan Januari 2020. Total jumlah bongkar barang pada bulan Januari 2021 di pelabuhan dalam Provinsi Aceh adalah 350.892 ton, sedangkan total jumlah muat barang adalah 127.933 ton. \n\nUntuk mendapatkan rilis resmi *BRS* ini 📰 silahkan download file dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/BRS_6.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/BRS_2.jpg')
        responded = True
    elif 'BRS5' in incoming_msg or 'Brs5' in incoming_msg or 'brs5' in incoming_msg:     
        text = '📉 *Berita Resmi Statistik*\n*_Nilai Tukar Petani, Inflasi Pedesaan dan Harga Produsen Gabah Provinsi Aceh Februari 2021_* 📰\n\nDi Provinsi Aceh pada Februari 2021, dihasilkan Nilai Tukar Petani sebesar 98,76 atau mengalami penurunan sebesar 0,27 persen. NTP gabungan ini sangat dipengaruhi oleh kelima Nilai Tukar Petani subsektor didalamnya. Terjadi penurunan Nilai Tukar Petani di semua subsektor selain subsektor peternakan. Indeks Harga yang Diterima Petani (It) pada Februari 2021 mengalami penurunan sebesar 0,47 persen dibanding periode sebelumnya. Hal ini disebabkan oleh turunnya It pada semua subsektor selain subsektor peternakan. Selama Februari 2021, Indeks Harga yang Dibayar Petani (Ib) di Provinsi Aceh turun sebesar 0,20 persen dibanding periode sebelumnya. Penurunan Ib tersebut terjadi pada semua subsektor. Dalam Provinsi Aceh selama Februari 2021, terjadi deflasi di perdesaan sebesar 0,27 persen. Deflasi tersebut disebabkan oleh penurunan harga pada kelompok makanan, minuman, dan tembakau sebesar 0,45 persen dengan rendahnya harga komoditas sayur-sayuran (cabai merah, bawang merah, dan kacang panjang) dan ikan (tongkol dan bandeng). Selama Februari 2021, harga gabah kualitas GKP di tingkat petani mengalami penurunan sebesar 4,87 persen atau senilai Rp. 238 menjadi 4.651 rupiah per kilogram. \n\nUntuk mendapatkan rilis resmi *BRS* ini 📰 silahkan download file dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/BRS_5.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/BRS_3.jpg')
        responded = True
        
    elif 'BRS4' in incoming_msg or 'Brs4' in incoming_msg or 'brs4' in incoming_msg:    
        text = '📉 *Berita Resmi Statistik*\n*_Perkembangan Ekspor dan Impor Provinsi Aceh Januari 2021_* 📰\n\nNilai ekspor barang asal Provinsi Aceh pada bulan Januari 2021 mengalami penurunan jika dibandingkan dengan bulan Desember 2020, nilai ekspor Provinsi Aceh sebesar 32.734.368 USD atau mengalami penurunan sebesar 0,71 persen. Kelompok komoditi non migas terbesar yang diekspor pada bulan Januari 2021 dari kelompok komoditi bahan Bakar Bakar Mineral yaitu sebesar 21.305.285 USD dengan komoditas utama berupa Coal, whether or not pulverised, but not agglomerated, other coal (Batubara yang dilumasi maupun tidak tapi tidak diaglomerasi, batubara lainnya). Ekspor komoditi non migas terbesar asal Provinsi Aceh selama bulan Januari 2021 ditujukan ke negara India yaitu sebesar 20.551.798 USD dengan komoditas utama berupa Coal, whether or not pulverised, but not agglomerated, other coal (Batubara yang dilumasi maupun tidak tapi tidak diaglomerasi, batubara lainnya). Nilai impor Provinsi Aceh pada bulan Januari 2021 tercatat sebesar 33.220 USD, mengalami penurunan sebesar 98,51 persen dibandingkan bulan Desember 2020. Selama bulan Januari 2021 nilai impor hanya berupa komoditas tunggal, yaitu mesin-mesin/pesawat mekanik sebesar 33.220 USD. Neraca perdagangan Provinsi Aceh pada bulan Januari 2021 mengalami surplus sebesar 32.701.148 USD, atau mengalami peningkatan sebesar 6,36 persen jika dibandingkan dengan bulan Desember 2020. \n\nUntuk mendapatkan rilis resmi *BRS* ini 📰 silahkan download file dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/BRS_4.pdf'
        msg.body(text)
        
        msg.media('https://github.com/habicahya/habicahya/raw/main/BRS_4.jpg')
        responded = True
        
    elif 'BRS3' in incoming_msg or 'Brs3' in incoming_msg or 'brs3' in incoming_msg:    
        text = '📉 *Berita Resmi Statistik*\n*_Luas Panen dan Produksi Padi di Provinsi Aceh 2020 (Angka Tetap)_* 📰\n\nLuas panen padi pada 2020 sebesar 317,87 ribu hektar, mengalami kenaikan sebanyak 7,86 ribu hektar atau 2,53 persen dibandingkan 2019 yang sebesar 310,01 ribu hektar. Produksi padi pada 2020 sebesar 1,76 juta ton gabah kering giling (GKG), mengalami kenaikan sebanyak 42,88 ribu ton atau 2,50 persen dibandingkan 2019 yang sebesar 1,71 juta ton GKG. Jika dilihat menurut subround, terjadi peningkatan produksi padi pada subround Januari-April dan September-Desember 2020, yaitu masing-masing sebesar 1,44 ribu ton GKG (0,18 persen) dan 91,71 ribu ton GKG (18,17 persen) dibandingkan 2019. Penurunan hanya terjadi pada subround Mei-Agustus, yakni sebesar 50,28 ribu ton GKG (12,24 persen). Jika dikonversikan menjadi beras untuk konsumsi pangan penduduk, produksi beras pada 2020 sebesar 1,01 juta ton, mengalami kenaikan sebanyak 24,58 ribu ton atau 2,50 persen dibandingkan 2019 yang sebesar 982,57 ribu ton. Potensi produksi padi pada subround Januari-April 2021 diperkirakan sebesar 790,43 ribu ton GKG, mengalami penurunan sebanyak 9,72 ribu ton atau 1,21 persen dibandingkan subround yang sama pada 2020 yang sebesar 800,15 ribu ton GKG.\n\nUntuk mendapatkan rilis resmi *BRS* ini 📰 silahkan download file dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/BRS_3.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/BRS_5.jpg')
        responded = True
        
    elif 'BRS2' in incoming_msg or 'Brs2' in incoming_msg or 'brs2' in incoming_msg:     
        text = '📉 *Berita Resmi Statistik*\n*_Hasil Sensus Penduduk Provinsi Aceh 2020_* 📰\n\nSensus Penduduk adalah merupakan amanat undang-undang No. 16 Tahun 1997  tentang statistik, yang dilaksakan sepuluh tahun sekali pada tahun yang berakhiran angka nol. Sensus Penduduk 2020 (SP2020) adalah merupakan sensus penduduk yang ketujuh sejak Indonesia Merdeka. \n\nUntuk mendapatkan rilis resmi *BRS* ini 📰 silahkan download file dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/BRS_2.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/BRS_6.jpg')
        responded = True
        
    elif 'BRS1' in incoming_msg or 'Brs1' in incoming_msg or 'brs1' in incoming_msg:           
        text = '📉 *Berita Resmi Statistik*\n*_Profil Kemiskinan Dan Ketimpangan Pengeluaran Penduduk Provinsi Aceh September 2020_* 📰\n\nPada Bulan September 2020, jumlah penduduk miskin di Aceh sebanyak 833,91 ribu orang (15,43 persen), bertambah sebanyak 19 ribu orang dibandingkan dengan penduduk miskin pada Maret 2020 yang jumlahnya 814,91 ribu orang (14,99 persen). Selama periode Maret 2020–September 2020, persentase penduduk miskin di daerah perdesaan dan  perkotaan mengalami kenaikan. Di perkotaan, persentase penduduk miskin naik sebesar 0,47 poin (dari 9,84 persen menjadi 10,31 persen), sedangkan di daerah perdesaan naik 0,50 poin (dari 17,46 persen menjadi 17,96 persen).  \n\nUntuk mendapatkan rilis resmi *BRS* ini 📰 silahkan download file dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/BRS_1.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/BRS_7.jpg')
        responded = True

    elif 'm2' in incoming_msg:
        text = publikasi()
        msg.body(text)
        responded = True

    elif 'PUB1' in incoming_msg or 'Pub1' in incoming_msg or 'pub1' in incoming_msg:
        text = dda()
        msg.body(text)
        responded = True
        
    elif 'DDA5' in incoming_msg or 'Dda5' in incoming_msg or 'dda5' in incoming_msg:
        text = '📘 *Publikasi Kota Subulussalam Dalam Angka Tahun 2021* 📊\n\nPublikasi ini menyajikan data sekunder yang berasal dari berbagai Dinas/Instansi/Lembaga dalam lingkungan Pemerintah Kota Subulussalam maupun non Pemerintah dan data-data hasil sensus dan survei yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/DDA_5.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/DDA1.jpg')
        responded = True
        
    elif 'DDA4' in incoming_msg or 'Dda4' in incoming_msg or 'dda4' in incoming_msg:
        text = '📘 *Publikasi Kota Subulussalam Dalam Angka Tahun 2020* 📊\n\nPublikasi ini menyajikan data sekunder yang berasal dari berbagai Dinas/Instansi/Lembaga dalam lingkungan Pemerintah Kota Subulussalam maupun non Pemerintah dan data-data hasil sensus dan survei yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/DDA_4.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/DDA2.jpg')
        responded = True        

    elif 'DDA3' in incoming_msg or 'Dda3' in incoming_msg or 'dda3' in incoming_msg:
        text = '📘 *Publikasi Kota Subulussalam Dalam Angka Tahun 2019* 📊\n\nPublikasi ini menyajikan data sekunder yang berasal dari berbagai Dinas/Instansi/Lembaga dalam lingkungan Pemerintah Kota Subulussalam maupun non Pemerintah dan data-data hasil sensus dan survei yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/DDA_3.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/DDA3.jpg')
        responded = True 

    elif 'DDA2' in incoming_msg or 'Dda2' in incoming_msg or 'dda2' in incoming_msg:
        text = '📘 *Publikasi Kota Subulussalam Dalam Angka Tahun 2018* 📊\n\nPublikasi ini menyajikan data sekunder yang berasal dari berbagai Dinas/Instansi/Lembaga dalam lingkungan Pemerintah Kota Subulussalam maupun non Pemerintah dan data-data hasil sensus dan survei yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/DDA_2.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/DDA4.jpg')
        responded = True 
 
    elif 'DDA1' in incoming_msg or 'Dda1' in incoming_msg or 'dda1' in incoming_msg:
        text = '📘 *Publikasi Kota Subulussalam Dalam Angka Tahun 2017* 📊\n\nPublikasi ini menyajikan data sekunder yang berasal dari berbagai Dinas/Instansi/Lembaga dalam lingkungan Pemerintah Kota Subulussalam maupun non Pemerintah dan data-data hasil sensus dan survei yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/DDA_1.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/DDA5.jpg')
        responded = True
               
    elif 'PUB2' in incoming_msg or 'Pub2' in incoming_msg or 'pub2' in incoming_msg:
        text = statda()
        msg.body(text)
        responded = True
        
    elif 'STATDA5' in incoming_msg or 'Statda5' in incoming_msg or 'statda5' in incoming_msg:
        text = '📗 *Publikasi Statistik Daerah Kota Subulussalam Tahun 2020* 📉\n\nDiterbitkan oleh Badan Pusat Statistik Kota Subulussalam berisi data dan informasi terpilih seputar Kota Subulussalam yang dianalisis secara sederhana untuk membantu pengguna data memahami perkembangan pembangunan serta potensi yang ada di Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/STATDA_5.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/STATDA1.jpg')
        responded = True
        
    elif 'STATDA4' in incoming_msg or 'Statda4' in incoming_msg or 'statda4' in incoming_msg:
        text = '📗 *Publikasi Statistik Daerah Kota Subulussalam Tahun 2019* 📉\n\nDiterbitkan oleh Badan Pusat Statistik Kota Subulussalam berisi data dan informasi terpilih seputar Kota Subulussalam yang dianalisis secara sederhana untuk membantu pengguna data memahami perkembangan pembangunan serta potensi yang ada di Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/STATDA_4.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/STATDA2.jpg')
        responded = True        

    elif 'STATDA3' in incoming_msg or 'Statda3' in incoming_msg or 'statda3' in incoming_msg:
        text = '📗 *Publikasi Statistik Daerah Kota Subulussalam Tahun 2018* 📉\n\nDiterbitkan oleh Badan Pusat Statistik Kota Subulussalam berisi data dan informasi terpilih seputar Kota Subulussalam yang dianalisis secara sederhana untuk membantu pengguna data memahami perkembangan pembangunan serta potensi yang ada di Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/STATDA_3.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/STATDA3.jpg')
        responded = True 

    elif 'STATDA2' in incoming_msg or 'Statda2' in incoming_msg or 'statda2' in incoming_msg:
        text = '📗 *Publikasi Statistik Daerah Kota Subulussalam Tahun 2017* 📉\n\nDiterbitkan oleh Badan Pusat Statistik Kota Subulussalam berisi data dan informasi terpilih seputar Kota Subulussalam yang dianalisis secara sederhana untuk membantu pengguna data memahami perkembangan pembangunan serta potensi yang ada di Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/STATDA_2.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/STATDA4.jpg')
        responded = True 
 
    elif 'STATDA1' in incoming_msg or 'Statda1' in incoming_msg or 'statda1' in incoming_msg:
        text = '📗 *Publikasi Statistik Daerah Kota Subulussalam Tahun 2016* 📉\n\nDiterbitkan oleh Badan Pusat Statistik Kota Subulussalam berisi data dan informasi terpilih seputar Kota Subulussalam yang dianalisis secara sederhana untuk membantu pengguna data memahami perkembangan pembangunan serta potensi yang ada di Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/STATDA_1.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/STATDA5.jpg')
        responded = True
        
    elif 'PUB3' in incoming_msg or 'Pub3' in incoming_msg or 'pub3' in incoming_msg:
        text = kcda()
        msg.body(text)
        responded = True
        
    elif 'KCDA1' in incoming_msg or 'Kcda1' in incoming_msg or 'kcda1' in incoming_msg:
        text = simpang()
        msg.body(text)
        responded = True       
        
    elif 'KCDA2' in incoming_msg or 'Kcda2' in incoming_msg or 'kcda2' in incoming_msg:
        text = penanggalan()
        msg.body(text)
        responded = True        
        
    elif 'KCDA3' in incoming_msg or 'Kcda3' in incoming_msg or 'kcda3' in incoming_msg:
        text = rundeng()
        msg.body(text)
        responded = True        
        
    elif 'KCDA4' in incoming_msg or 'Kcda4' in incoming_msg or 'kcda4' in incoming_msg:
        text = sultan()
        msg.body(text)
        responded = True
        
    elif 'KCDA5' in incoming_msg or 'Kcda5' in incoming_msg or 'kcda5' in incoming_msg:
        text =longkib()
        msg.body(text)
        responded = True        

    elif 'SIMPANGKIRI5' in incoming_msg or 'Simpangkiri5' in incoming_msg or 'simpangkiri5' in incoming_msg or 'SimpangKiri5' in incoming_msg:
        text = '📕 *Publikasi Kecamatan Simpang Kiri Dalam Angka Tahun 2020* 🏡\n\nMerupakan hasil pengumpulan data yang berasal dari lapangan pada Kecamatan Simpang Kiri dalam Kota Subulussalam dan data-data hasil pendataan yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/SIMPANGKIRI_5.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/SIMPANG1.jpg')
        responded = True

    elif 'SIMPANGKIRI4' in incoming_msg or 'Simpangkiri4' in incoming_msg or 'simpangkiri4' in incoming_msg or 'SimpangKiri4' in incoming_msg:
        text = '📕 *Publikasi Kecamatan Simpang Kiri Dalam Angka Tahun 2019* 🏡\n\nMerupakan hasil pengumpulan data yang berasal dari lapangan pada Kecamatan Simpang Kiri dalam Kota Subulussalam dan data-data hasil pendataan yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/SIMPANGKIRI_4.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/SIMPANG2.jpg')
        responded = True

    elif 'SIMPANGKIRI3' in incoming_msg or 'Simpangkiri3' in incoming_msg or 'simpangkiri3' in incoming_msg or 'SimpangKiri3' in incoming_msg:
        text = '📕 *Publikasi Kecamatan Simpang Kiri Dalam Angka Tahun 2018* 🏡\n\nMerupakan hasil pengumpulan data yang berasal dari lapangan pada Kecamatan Simpang Kiri dalam Kota Subulussalam dan data-data hasil pendataan yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/SIMPANGKIRI_3.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/SIMPANG3.jpg')
        responded = True

    elif 'SIMPANGKIRI2' in incoming_msg or 'Simpangkiri2' in incoming_msg or 'simpangkiri2' in incoming_msg or 'SimpangKiri2' in incoming_msg:
        text = '📕 *Publikasi Kecamatan Simpang Kiri Dalam Angka Tahun 2017* 🏡\n\nMerupakan hasil pengumpulan data yang berasal dari lapangan pada Kecamatan Simpang Kiri dalam Kota Subulussalam dan data-data hasil pendataan yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/SIMPANGKIRI_2.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/SIMPANG4.jpg')
        responded = True

    elif 'SIMPANGKIRI1' in incoming_msg or 'Simpangkiri1' in incoming_msg or 'simpangkiri1' in incoming_msg or 'SimpangKiri1' in incoming_msg:
        text = '📕 *Publikasi Kecamatan Simpang Kiri Dalam Angka Tahun 2016* 🏡\n\nMerupakan hasil pengumpulan data yang berasal dari lapangan pada Kecamatan Simpang Kiri dalam Kota Subulussalam dan data-data hasil pendataan yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/SIMPANGKIRI_1.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/SIMPANG5.jpg')
        responded = True        

    elif 'PENANGGALAN5' in incoming_msg or 'Penanggalan5' in incoming_msg or 'penanggalan5' in incoming_msg or 'Penang5' in incoming_msg:
        text = '📕 *Publikasi Kecamatan Penanggalan Dalam Angka Tahun 2020* 🏡\n\nMerupakan hasil pengumpulan data yang berasal dari lapangan pada Kecamatan Penanggalan dalam Kota Subulussalam dan data-data hasil pendataan yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/PENANGGALAN_5.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/PENANG1.jpg')
        responded = True        

    elif 'PENANGGALAN4' in incoming_msg or 'Penanggalan4' in incoming_msg or 'penanggalan4' in incoming_msg or 'Penang4' in incoming_msg:
        text = '📕 *Publikasi Kecamatan Penanggalan Dalam Angka Tahun 2019* 🏡\n\nMerupakan hasil pengumpulan data yang berasal dari lapangan pada Kecamatan Penanggalan dalam Kota Subulussalam dan data-data hasil pendataan yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/PENANGGALAN_4.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/PENANG2.jpg')
        responded = True 

    elif 'PENANGGALAN3' in incoming_msg or 'Penanggalan3' in incoming_msg or 'penanggalan3' in incoming_msg or 'Penang3' in incoming_msg:
        text = '📕 *Publikasi Kecamatan Penanggalan Dalam Angka Tahun 2018* 🏡\n\nMerupakan hasil pengumpulan data yang berasal dari lapangan pada Kecamatan Penanggalan dalam Kota Subulussalam dan data-data hasil pendataan yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/PENANGGALAN_3.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/PENANG3.jpg')
        responded = True 

    elif 'PENANGGALAN2' in incoming_msg or 'Penanggalan2' in incoming_msg or 'penanggalan2' in incoming_msg or 'Penang2' in incoming_msg:
        text = '📕 *Publikasi Kecamatan Penanggalan Dalam Angka Tahun 2017* 🏡\n\nMerupakan hasil pengumpulan data yang berasal dari lapangan pada Kecamatan Penanggalan dalam Kota Subulussalam dan data-data hasil pendataan yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/PENANGGALAN_2.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/PENANG4.jpg')
        responded = True 

    elif 'PENANGGALAN1' in incoming_msg or 'Penanggalan1' in incoming_msg or 'penanggalan1' in incoming_msg or 'Penang1' in incoming_msg:
        text = '📕 *Publikasi Kecamatan Penanggalan Dalam Angka Tahun 2016* 🏡\n\nMerupakan hasil pengumpulan data yang berasal dari lapangan pada Kecamatan Penanggalan dalam Kota Subulussalam dan data-data hasil pendataan yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/PENANGGALAN_1.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/PENANG5.jpg')
        responded = True         

    elif 'RUNDENG5' in incoming_msg or 'Rundeng5' in incoming_msg or 'rundeng5' in incoming_msg:
        text = '📕 *Publikasi Kecamatan Rundeng Dalam Angka Tahun 2020* 🏡\n\nMerupakan hasil pengumpulan data yang berasal dari lapangan pada Kecamatan Rundeng dalam Kota Subulussalam dan data-data hasil pendataan yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/RUNDENG_5.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/RUNDENG1.jpg')
        responded = True

    elif 'RUNDENG4' in incoming_msg or 'Rundeng4' in incoming_msg or 'rundeng4' in incoming_msg:
        text = '📕 *Publikasi Kecamatan Rundeng Dalam Angka Tahun 2019* 🏡\n\nMerupakan hasil pengumpulan data yang berasal dari lapangan pada Kecamatan Rundeng dalam Kota Subulussalam dan data-data hasil pendataan yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/RUNDENG_4.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/RUNDENG2.jpg')
        responded = True
        
    elif 'RUNDENG3' in incoming_msg or 'Rundeng3' in incoming_msg or 'rundeng3' in incoming_msg:
        text = '📕 *Publikasi Kecamatan Rundeng Dalam Angka Tahun 2018* 🏡\n\nMerupakan hasil pengumpulan data yang berasal dari lapangan pada Kecamatan Rundeng dalam Kota Subulussalam dan data-data hasil pendataan yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/RUNDENG_3.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/RUNDENG3.jpg')
        responded = True

    elif 'RUNDENG2' in incoming_msg or 'Rundeng2' in incoming_msg or 'rundeng2' in incoming_msg:
        text = '📕 *Publikasi Kecamatan Rundeng Dalam Angka Tahun 2017* 🏡\n\nMerupakan hasil pengumpulan data yang berasal dari lapangan pada Kecamatan Rundeng dalam Kota Subulussalam dan data-data hasil pendataan yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/RUNDENG_2.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/RUNDENG4.jpg')
        responded = True

    elif 'RUNDENG1' in incoming_msg or 'Rundeng1' in incoming_msg or 'rundeng1' in incoming_msg:
        text = '📕 *Publikasi Kecamatan Rundeng Dalam Angka Tahun 2016* 🏡\n\nMerupakan hasil pengumpulan data yang berasal dari lapangan pada Kecamatan Rundeng dalam Kota Subulussalam dan data-data hasil pendataan yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/RUNDENG_1.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/RUNDENG5.jpg')
        responded = True
  
    elif 'SULTANDAULAT5' in incoming_msg or 'Sultandaulat5' in incoming_msg or 'sultandaulat5' in incoming_msg or 'Sultan5' in incoming_msg or 'Daulat5' in incoming_msg:
        text = '📕 *Publikasi Kecamatan Sultan Daulat Dalam Angka Tahun 2020* 🏡\n\nMerupakan hasil pengumpulan data yang berasal dari lapangan pada Kecamatan Sultan Daulat dalam Kota Subulussalam dan data-data hasil pendataan yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/SULTANDAULAT_5.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/SULTAN1.jpg')
        responded = True        

    elif 'SULTANDAULAT4' in incoming_msg or 'Sultandaulat4' in incoming_msg or 'sultandaulat4' in incoming_msg or 'Sultan4' in incoming_msg or 'Daulat4' in incoming_msg:
        text = '📕 *Publikasi Kecamatan Sultan Daulat Dalam Angka Tahun 2019* 🏡\n\nMerupakan hasil pengumpulan data yang berasal dari lapangan pada Kecamatan Sultan Daulat dalam Kota Subulussalam dan data-data hasil pendataan yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/SULTANDAULAT_4.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/SULTAN2.jpg')
        responded = True 
        
    elif 'SULTANDAULAT3' in incoming_msg or 'Sultandaulat3' in incoming_msg or 'sultandaulat3' in incoming_msg or 'Sultan3' in incoming_msg or 'Daulat3' in incoming_msg:
        text = '📕 *Publikasi Kecamatan Sultan Daulat Dalam Angka Tahun 2018* 🏡\n\nMerupakan hasil pengumpulan data yang berasal dari lapangan pada Kecamatan Sultan Daulat dalam Kota Subulussalam dan data-data hasil pendataan yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/SULTANDAULAT_3.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/SULTAN3.jpg')
        responded = True 
        
    elif 'SULTANDAULAT2' in incoming_msg or 'Sultandaulat2' in incoming_msg or 'sultandaulat2' in incoming_msg or 'Sultan2' in incoming_msg or 'Daulat2' in incoming_msg:
        text = '📕 *Publikasi Kecamatan Sultan Daulat Dalam Angka Tahun 2017* 🏡\n\nMerupakan hasil pengumpulan data yang berasal dari lapangan pada Kecamatan Sultan Daulat dalam Kota Subulussalam dan data-data hasil pendataan yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/SULTANDAULAT_2.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/SULTAN4.jpg')
        responded = True         
        
    elif 'SULTANDAULAT1' in incoming_msg or 'Sultandaulat1' in incoming_msg or 'sultandaulat1' in incoming_msg or 'Sultan1' in incoming_msg or 'Daulat1' in incoming_msg:
        text = '📕 *Publikasi Kecamatan Sultan Daulat Dalam Angka Tahun 2016* 🏡\n\nMerupakan hasil pengumpulan data yang berasal dari lapangan pada Kecamatan Sultan Daulat dalam Kota Subulussalam dan data-data hasil pendataan yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/SULTANDAULAT_1.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/SULTAN5.jpg')
        responded = True 

    elif 'LONGKIB5' in incoming_msg or 'Longkib5' in incoming_msg or 'longkib5' in incoming_msg:
        text = '📕 *Publikasi Kecamatan Longkib Dalam Angka Tahun 2020* 🏡\n\nMerupakan hasil pengumpulan data yang berasal dari lapangan pada Kecamatan Longkib dalam Kota Subulussalam dan data-data hasil pendataan yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/LONGKIB_5.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/LONKIB1.jpg')
        responded = True
                
    elif 'LONGKIB4' in incoming_msg or 'Longkib4' in incoming_msg or 'longkib4' in incoming_msg:
        text = '📕 *Publikasi Kecamatan Longkib Dalam Angka Tahun 2019* 🏡\n\nMerupakan hasil pengumpulan data yang berasal dari lapangan pada Kecamatan Longkib dalam Kota Subulussalam dan data-data hasil pendataan yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/LONGKIB_4.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/LONKIB2.jpg')
        responded = True

    elif 'LONGKIB3' in incoming_msg or 'Longkib3' in incoming_msg or 'longkib3' in incoming_msg:
        text = '📕 *Publikasi Kecamatan Longkib Dalam Angka Tahun 2018* 🏡\n\nMerupakan hasil pengumpulan data yang berasal dari lapangan pada Kecamatan Longkib dalam Kota Subulussalam dan data-data hasil pendataan yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/LONGKIB_3.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/LONKIB3.jpg')
        responded = True

    elif 'LONGKIB2' in incoming_msg or 'Longkib2' in incoming_msg or 'longkib2' in incoming_msg:
        text = '📕 *Publikasi Kecamatan Longkib Dalam Angka Tahun 2017* 🏡\n\nMerupakan hasil pengumpulan data yang berasal dari lapangan pada Kecamatan Longkib dalam Kota Subulussalam dan data-data hasil pendataan yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/LONGKIB_2.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/LONKIB4.jpg')
        responded = True

    elif 'LONGKIB1' in incoming_msg or 'Longkib1' in incoming_msg or 'longkib1' in incoming_msg:
        text = '📕 *Publikasi Kecamatan Longkib Dalam Angka Tahun 2016* 🏡\n\nMerupakan hasil pengumpulan data yang berasal dari lapangan pada Kecamatan Longkib dalam Kota Subulussalam dan data-data hasil pendataan yang dilakukan oleh Badan Pusat Statistik Kota Subulussalam. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/LONGKIB_1.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/LONKIB5.jpg')
        responded = True

    elif 'PUB4' in incoming_msg or 'Pub4' in incoming_msg or 'pub4' in incoming_msg:
        text = pdrb()
        msg.body(text)
        responded = True
        
    elif 'PDRB4' in incoming_msg or 'Pdrb4' in incoming_msg or 'pdrb4' in incoming_msg:
        text = '📙 *Publikasi Produk Domestik Regional Bruto (PDRB) menurut Lapangan Usaha Kota Subulussalam tahun 2015-2019* 📈 \n\nMerupakan publikasi tahunan yang diterbitkan oleh Badan Pusat Statistik Kota Subulussalam. Sebagai kelanjutan dari publikasi sebelumnya, publikasi ini menyajikan tinjauan tentang perkembangan ekonomi makro Kota Subulussalam dalam kurun waktu lima tahun terakhir (2015-2019). Data PDRB dalam publikasi ini serta publikasi-publikasi selanjutnya mengunakan tahun dasar 2010, serta sudah menerapkan konsep System of National Accounts 2008 seperti yang direkomendasikan oleh PBB. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/PDRB_4.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/PDRB1.jpg')
        responded = True

    elif 'PDRB3' in incoming_msg or 'Pdrb3' in incoming_msg or 'pdrb3' in incoming_msg:
        text = '📙 *Publikasi Produk Domestik Regional Bruto (PDRB) menurut Lapangan Usaha Kota Subulussalam tahun 2014-2018* 📈 \n\nmerupakan publikasi tahunan yang diterbitkan oleh Badan Pusat Statistik Kota Subulussalam. Sebagai kelanjutan dari publikasi sebelumnya, publikasi ini menyajikan tinjauan tentang perkembangan ekonomi makro Kota Subulussalam dalam kurun waktu lima tahun terakhir (2014-2018). Data PDRB dalam publikasi ini serta publikasi-publikasi selanjutnya mengunakan tahun dasar 2010, serta sudah menerapkan konsep System of National Accounts 2008 seperti yang direkomendasikan oleh PBB. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/PDRB_3.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/PDRB2.jpg')
        responded = True

    elif 'PDRB2' in incoming_msg or 'Pdrb2' in incoming_msg or 'pdrb2' in incoming_msg:
        text = '📙 *Publikasi Produk Domestik Regional Bruto (PDRB) menurut Lapangan Usaha Kota Subulussalam tahun 2013-2017* 📈 \n\nmerupakan publikasi tahunan yang diterbitkan oleh Badan Pusat Statistik Kota Subulussalam. Sebagai kelanjutan dari publikasi sebelumnya, publikasi ini menyajikan tinjauan tentang perkembangan ekonomi makro Kota Subulussalam dalam kurun waktu lima tahun terakhir (2013-2017). Data PDRB dalam publikasi ini serta publikasi-publikasi selanjutnya mengunakan tahun dasar 2010, serta sudah menerapkan konsep System of National Accounts 2008 seperti yang direkomendasikan oleh PBB. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/PDRB_2.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/PDRB3.jpg')
        responded = True

    elif 'PDRB1' in incoming_msg or 'Pdrb1' in incoming_msg or 'pdrb1' in incoming_msg:
        text = '📙 *Publikasi Produk Domestik Regional Bruto (PDRB) menurut Lapangan Usaha Kota Subulussalam tahun 2011-2015* 📈 \n\nmerupakan publikasi tahunan yang diterbitkan oleh Badan Pusat Statistik Kota Subulussalam. Sebagai kelanjutan dari publikasi sebelumnya, publikasi ini menyajikan tinjauan tentang perkembangan ekonomi makro Kota Subulussalam dalam kurun waktu lima tahun terakhir (2011-2015). Data PDRB dalam publikasi ini serta publikasi-publikasi selanjutnya mengunakan tahun dasar 2010, serta sudah menerapkan konsep System of National Accounts 2008 seperti yang direkomendasikan oleh PBB. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/PDRB_1.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/PDRB4.jpg')
        responded = True

    elif 'PDRB5' in incoming_msg or 'Pdrb5' in incoming_msg or 'pdrb5' in incoming_msg:
        text = '📙 *Publikasi Produk Domestik Regional Bruto (PDRB) menurut Lapangan Usaha Kota Subulussalam tahun 2016-2020* 📈 \n\nmerupakan publikasi tahunan yang diterbitkan oleh Badan Pusat Statistik Kota Subulussalam. Sebagai kelanjutan dari publikasi sebelumnya, publikasi ini menyajikan tinjauan tentang perkembangan ekonomi makro Kota Subulussalam dalam kurun waktu lima tahun terakhir (2016-2020). Data PDRB dalam publikasi ini serta publikasi-publikasi selanjutnya mengunakan tahun dasar 2010, serta sudah menerapkan konsep System of National Accounts 2008 seperti yang direkomendasikan oleh PBB. \n\nPublikasi dapat di unduh melalui tautan dibawah ini 👇\nhttps://github.com/bpskotasubulussalam/data/raw/main/PDRB_5.pdf'
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/PDRB6.jpg')
        responded = True
    
    elif 'm3' in incoming_msg or 'Hello' in incoming_msg:
        reply = ("Hallo 🙋 Sahabat Data \nIni adalah menu *Pencarian Data* 🔎\n\n"
                 "Anda dapat melakukan pencarian data yang Anda inginkan dengan menuliskan pertanyaan langsung pada *Chat_Bot* 💬 ini.\n"
                 "*Contoh Penulisan* untuk pencarian data pada menu ini dapat dilakukan seperti berikut: 📝\n\n"
                 "👉 Berapa angka kemiskinan di kota subulussalam?\n"
                 "👉 Berapa jumlah penduduk di Provinsi Aceh?\n"
                 "👉 Berapa angka pengangguran di Indonesia?\n"
                 "👉 Berapa jumlah pengangguran di Kota Subulussalam?\n"
                 "👉 Berapa angka pertumbuhan ekonomi di Provinsi Aceh?\n"
                 "👉 Dll"
                 "\n\nSilahkan tuliskan pertanyaan Anda Atau ketik *Menu* untuk kembali ke menu utama")

        msg.body(reply)
        responded = True
    
    elif 'kemiskinan' in incoming_msg or 'miskin' in incoming_msg:
        # this question is about how many matches the team played
        incoming_msg2 = 'kemiskinan'
        cari_var = re.findall('|'.join(all_var), incoming_msg2) 
        if 'subulussalam' in incoming_msg or 'subussalam' in incoming_msg:
            result = df[df['Subulussalam'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Kota Subulussalam adalah {result2}.'
            msg.body(text)
        elif 'aceh' in incoming_msg or 'provinsi' in incoming_msg:
            result = df[df['Aceh'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Provinsi Aceh adalah {result2}.'
            msg.body(text)
        elif 'indonesia' in incoming_msg or 'nasional' in incoming_msg:
            result = df[df['Indonesia'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Indonesia adalah {result2}.'
            msg.body(text)
        else:
          msg.body('Maaf pilihan Anda tidak terdapat dalam menu kami, silahkan ketik *Menu* untuk kembali ke menu utama')
    
    elif 'pengangguran' in incoming_msg or 'nganggur' in incoming_msg:
        # this question is about how many matches the team played
        incoming_msg2 = 'pengangguran'
        cari_var = re.findall('|'.join(all_var), incoming_msg2) 
        if 'subulussalam' in incoming_msg or 'subussalam' in incoming_msg:
            result = df[df['Subulussalam'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Kota Subulussalam adalah {result2}.'
            msg.body(text)
        elif 'aceh' in incoming_msg or 'provinsi' in incoming_msg:
            result = df[df['Aceh'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Provinsi Aceh adalah {result2}.'
            msg.body(text)
        elif 'indonesia' in incoming_msg or 'nasional' in incoming_msg:
            result = df[df['Indonesia'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Indonesia adalah {result2}.'
            msg.body(text)
        else:
          msg.body('Maaf pilihan Anda tidak terdapat dalam menu kami, silahkan ketik *Menu* untuk kembali ke menu utama')
    
    elif 'penduduk' in incoming_msg:
        # this question is about how many matches the team played
        incoming_msg2 = 'penduduk'
        cari_var = re.findall('|'.join(all_var), incoming_msg2) 
        if 'subulussalam' in incoming_msg or 'subussalam' in incoming_msg:
            result = df[df['Subulussalam'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Kota Subulussalam adalah {result2}.'
            msg.body(text)
        elif 'aceh' in incoming_msg or 'provinsi' in incoming_msg:
            result = df[df['Aceh'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Provinsi Aceh adalah {result2}.'
            msg.body(text)
        elif 'indonesia' in incoming_msg or 'nasional' in incoming_msg:
            result = df[df['Indonesia'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Indonesia adalah {result2}.'
            msg.body(text)
        else:
          msg.body('Maaf pilihan Anda tidak terdapat dalam menu kami, silahkan ketik *Menu* untuk kembali ke menu utama')
 
    elif 'pertumbuhanekonomi' in incoming_msg or 'ekonomi' in incoming_msg:
        # this question is about how many matches the team played
        incoming_msg2 = 'pertumbuhanekonomi'
        cari_var = re.findall('|'.join(all_var), incoming_msg2) 
        if 'subulussalam' in incoming_msg or 'subussalam' in incoming_msg:
            result = df[df['Subulussalam'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Kota Subulussalam adalah {result2}.'
            msg.body(text)
        elif 'aceh' in incoming_msg or 'provinsi' in incoming_msg:
            result = df[df['Aceh'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Provinsi Aceh adalah {result2}.'
            msg.body(text)
        elif 'indonesia' in incoming_msg or 'nasional' in incoming_msg:
            result = df[df['Indonesia'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Indonesia adalah {result2}.'
            msg.body(text)
        else:
          msg.body('Maaf pilihan Anda tidak terdapat dalam menu kami, silahkan ketik *Menu* untuk kembali ke menu utama')    
    
    elif 'pdrb' in incoming_msg or 'produkdomestikregionalbruto' in incoming_msg or 'pdrbhargaberlaku' in incoming_msg or 'pdrbhb' in incoming_msg:
        # this question is about how many matches the team played
        incoming_msg2 = 'pdrbhb'
        cari_var = re.findall('|'.join(all_var), incoming_msg2) 
        if 'subulussalam' in incoming_msg or 'subussalam' in incoming_msg:
            result = df[df['Subulussalam'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Kota Subulussalam adalah {result2}.'
            msg.body(text)
        elif 'aceh' in incoming_msg or 'provinsi' in incoming_msg:
            result = df[df['Aceh'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Provinsi Aceh adalah {result2}.'
            msg.body(text)
        elif 'indonesia' in incoming_msg or 'nasional' in incoming_msg:
            result = df[df['Indonesia'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Indonesia adalah {result2}.'
            msg.body(text)
        else:
          msg.body('Maaf pilihan Anda tidak terdapat dalam menu kami, silahkan ketik *Menu* untuk kembali ke menu utama')    
    
    elif 'ipm' in incoming_msg or 'indekspembangunanmanusia' in incoming_msg or 'pembangunanmanusia' in incoming_msg:
        # this question is about how many matches the team played
        incoming_msg2 = 'ipm'
        cari_var = re.findall('|'.join(all_var), incoming_msg2) 
        if 'subulussalam' in incoming_msg or 'subussalam' in incoming_msg:
            result = df[df['Subulussalam'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Kota Subulussalam adalah {result2}.'
            msg.body(text)
        elif 'aceh' in incoming_msg or 'provinsi' in incoming_msg:
            result = df[df['Aceh'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Provinsi Aceh adalah {result2}.'
            msg.body(text)
        elif 'indonesia' in incoming_msg or 'nasional' in incoming_msg:
            result = df[df['Indonesia'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Indonesia adalah {result2}.'
            msg.body(text)
        else:
          msg.body('Maaf pilihan Anda tidak terdapat dalam menu kami, silahkan ketik *Menu* untuk kembali ke menu utama')      
    
    elif 'ahh' in incoming_msg or 'angkaharapanhidup' in incoming_msg or 'harapanhidup' in incoming_msg:
        # this question is about how many matches the team played
        incoming_msg2 = 'ahh'
        cari_var = re.findall('|'.join(all_var), incoming_msg2) 
        if 'subulussalam' in incoming_msg or 'subussalam' in incoming_msg:
            result = df[df['Subulussalam'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Kota Subulussalam adalah {result2}.'
            msg.body(text)
        elif 'aceh' in incoming_msg or 'provinsi' in incoming_msg:
            result = df[df['Aceh'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Provinsi Aceh adalah {result2}.'
            msg.body(text)
        elif 'indonesia' in incoming_msg or 'nasional' in incoming_msg:
            result = df[df['Indonesia'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Indonesia adalah {result2}.'
            msg.body(text)
        else:
          msg.body('Maaf pilihan Anda tidak terdapat dalam menu kami, silahkan ketik *Menu* untuk kembali ke menu utama')
    
    elif 'ipg' in incoming_msg or 'indekspembangunangender' in incoming_msg or 'pembangunangender' in incoming_msg:
        # this question is about how many matches the team played
        incoming_msg2 = 'ipg'
        cari_var = re.findall('|'.join(all_var), incoming_msg2) 
        if 'subulussalam' in incoming_msg or 'subussalam' in incoming_msg:
            result = df[df['Subulussalam'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Kota Subulussalam adalah {result2}.'
            msg.body(text)
        elif 'aceh' in incoming_msg or 'provinsi' in incoming_msg:
            result = df[df['Aceh'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Provinsi Aceh adalah {result2}.'
            msg.body(text)
        elif 'indonesia' in incoming_msg or 'nasional' in incoming_msg:
            result = df[df['Indonesia'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Indonesia adalah {result2}.'
            msg.body(text)
        else:
          msg.body('Maaf pilihan Anda tidak terdapat dalam menu kami, silahkan ketik *Menu* untuk kembali ke menu utama')

    elif 'rata-ratalamasekolah' in incoming_msg or 'mys' in incoming_msg or 'lamasekolah' in incoming_msg:
        # this question is about how many matches the team played
        incoming_msg2 = 'rataratalamasekolah'
        cari_var = re.findall('|'.join(all_var), incoming_msg2) 
        if 'subulussalam' in incoming_msg or 'subussalam' in incoming_msg:
            result = df[df['Subulussalam'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Kota Subulussalam adalah {result2}.'
            msg.body(text)
        elif 'aceh' in incoming_msg or 'provinsi' in incoming_msg:
            result = df[df['Aceh'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Provinsi Aceh adalah {result2}.'
            msg.body(text)
        elif 'indonesia' in incoming_msg or 'nasional' in incoming_msg:
            result = df[df['Indonesia'] == cari_var[0]][df.columns[4:10]]
            result2 = result.reset_index().T
            text = f'📁 Data {cari_var[0]} \ndi Indonesia adalah {result2}.'
            msg.body(text)
        else:
          msg.body('Maaf pilihan Anda tidak terdapat dalam menu kami, silahkan ketik *Menu* untuk kembali ke menu utama')
    
    elif 'm4' in incoming_msg:
        # return total cases
        text = layanan()
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/Moto_BPS.jpeg')
        responded = True

    elif 'm5' in incoming_msg:
        # return total cases
        text = tentang()
        msg.body(text)
        msg.media('https://github.com/habicahya/habicahya/raw/main/BPS_About_Us.jpeg')
        responded = True
        
    elif responded == False:
       msg.body('Maaf kode yang Anda masukan salah, silahkan masukan *Kode* yang benar atau ketik *Menu* untuk kembali ke Menu Utama')
    
    return str(resp)
    
def menu():

    menu = 'Hallo 🙋🏽‍♂, Sahabat Data. \nIni adalah layanan *Chat_Bot* 💬 \n*Badan Pusat Statistik* \n*Kota Subulussalam* 🏢 \n\nAnda bisa mendapatkan informasi terbaru tentang Statistik Kota Subulussalam langsung dari handphone.📱\n\nSilahkan pilih menu di bawah ini untuk memulai 👇 \n\n *M1*. Berita Resmi Statistik. \n *M2*. Publikasi Statistik \n *M3*. Pencarian Data \n *M4*. Layanan di BPS Kota Subulussalam. \n *M5*. Tentang Kami.\n\nSilahkan masukan *Kode* layanan yang Anda perlukan.\nContoh : *M1*'
    
    return menu


def brs():
    brs = '*BERITA RESMI STATISTIK (BRS)* 📰\n*BPS Kota Subulussalam* 🏢 \n\n\
✅ *FEBRUARI 2021*\n\n\
*BRS1*\n_Profil Kemiskinan Dan Ketimpangan Pengeluaran Penduduk Provinsi Aceh September 2020_\n\
*BRS2*\n_Hasil Sensus Penduduk Provinsi Aceh 2020_\n\n\
✅ *MARET 2021*\n\n\
*BRS3*\n_Luas Panen dan Produksi Padi di Provinsi Aceh 2020 (Angka Tetap)_\n\
*BRS4*\n_Perkembangan Ekspor dan Impor Provinsi Aceh Januari 2021_\n\
*BRS5*\n_Nilai Tukar Petani, Inflasi Pedesaan dan Harga Produsen Gabah Provinsi Aceh Februari 2021_\n\
*BRS6*\n_Perkembangan Transportasi dan Pariwisata Provinsi Aceh Januari 2021_\n\
*BRS7*\n_Indeks Harga Konsumen/Inflasi Provinsi Aceh Februari 2021_\n\n\
Silahkan masukan *Kode BRS* 📰 untuk menampilkan BRS yang Anda inginkan.\nContoh : *BRS1* atau ketik *Menu* untuk kembali ke menu utama'
    return brs
      
def publikasi():
    publikasi='*PUBLIKASI STATISTIK* 📗\n*BPS Kota Subulussalam* 🏢\n\n\
Silahkan pilih *Publikasi* yang ingin ditampilkan\n\n\
✅ *PUB1*\n_Kota Subulussalam Dalam Angka_\n\
✅ *PUB2*\n_Statistik Daerah Kota Subulussalam_\n\
✅ *PUB3*\n_Kecamatan Dalam Angka_\n\
✅ *PUB4*\n_Produk Domestik Regional Bruto (PDRB) Menurut Lapangan Usaha_\n\n\
Silahkan masukan *Kode Publikasi* 📗 untuk menampilkan Publikasi Statistik yang Anda inginkan.\nContoh : *PUB1* atau ketik *Menu* untuk kembali ke menu utama'
    return publikasi

def dda():
    dda='*PUBLIKASI STATISTIK* 📘\n*SUBULUSSALAM DALAM ANGKA* 📊\n\n\
Silahkan pilih publikasi yang ingin ditampilkan\n\n\
✅ *DDA1*\n_Kota Subulussalam Dalam Angka Tahun 2017_\n\
✅ *DDA2*\n_Kota Subulussalam Dalam Angka Tahun 2018_\n\
✅ *DDA3*\n_Kota Subulussalam Dalam Angka Tahun 2019_\n\
✅ *DDA4*\n_Kota Subulussalam Dalam Angka Tahun 2020_\n\
✅ *DDA5*\n_Kota Subulussalam Dalam Angka Tahun 2021_\n\n\
Silahkan masukan *Kode Publikasi* 📘 untuk menampilkan Publikasi yang Anda inginkan.\nContoh : *DDA1* atau ketik *Menu* untuk kembali ke menu utama'
    return dda

def statda():
    statda='*PUBLIKASI STATISTIK* 📗\n*STATDA KOTA SUBULUSSALAM* 📉\n\n\
Silahkan pilih publikasi yang ingin ditampilkan\n\n\
✅ *STATDA1*\n_Statistik Daerah Kota Subulussalam Tahun 2016_\n\
✅ *STATDA2*\n_Statistik Daerah Kota Subulussalam Tahun 2017_\n\
✅ *STATDA3*\n_Statistik Daerah Kota Subulussalam Tahun 2018_\n\
✅ *STATDA4*\n_Statistik Daerah Kota Subulussalam Tahun 2019_\n\
✅ *STATDA5*\n_Statistik Daerah Kota Subulussalam Tahun 2020_\n\n\
Silahkan masukan *Kode Publikasi* 📗 untuk menampilkan Publikasi yang Anda inginkan.\nContoh : *STATDA1* atau ketik *Menu* untuk kembali ke menu utama'
    return statda

def kcda():
    kcda='*PUBLIKASI STATISTIK* 📕\n*KECAMATAN DALAM ANGKA* 🏡\n\n\
Silahkan pilih Kecamatan yang ingin ditampilkan\n\n\
✅ *KCDA1*\n_Kecamatan Simpang Kiri Dalam Angka_\n\
✅ *KCDA2*\n_Kecamatan Penanggalan Dalam Angka_\n\
✅ *KCDA3*\n_Kecamatan Rundeng Dalam Angka_\n\
✅ *KCDA4*\n_Kecamatan Sultan Daulat Dalam Angka_\n\
✅ *KCDA5*\n_Kecamatan Longkib Dalam Angka_\n\n\
Silahkan masukan *Kode Publikasi* 📕 untuk menampilkan Kecamatan yang Anda inginkan.\nContoh : *KCDA1* atau ketik *Menu* untuk kembali ke menu utama'
    return kcda

def simpang():
    simpang='*PUBLIKASI KECAMATAN SIMPANG KIRI DALAM ANGKA* 📕\n\n\
Silahkan pilih publikasi yang ingin ditampilkan\n\n\
✅ *SIMPANGKIRI1*\n_Kecamatan Simpang Kiri Dalam Angka Tahun 2016_\n\
✅ *SIMPANGKIRI2*\n_Kecamatan Simpang Kiri Dalam Angka Tahun 2017_\n\
✅ *SIMPANGKIRI3*\n_Kecamatan Simpang Kiri Dalam Angka Tahun 2018_\n\
✅ *SIMPANGKIRI4*\n_Kecamatan Simpang Kiri Dalam Angka Tahun 2019_\n\
✅ *SIMPANGKIRI5*\n_Kecamatan Simpang Kiri Dalam Angka Tahun 2020_\n\n\
Silahkan masukan *Kode Publikasi* 📕 untuk menampilkan Publikasi yang Anda inginkan.\nContoh : *SIMPANGKIRI1* atau ketik *Menu* untuk kembali ke menu utama'
    return simpang

def penanggalan():
    penanggalan='*PUBLIKASI KECAMATAN PENANGGALAN DALAM ANGKA* 📕\n\n\
Silahkan pilih publikasi yang ingin ditampilkan\n\n\
✅ *PENANGGALAN1*\n_Kecamatan Penanggalan Dalam Angka Tahun 2016_\n\
✅ *PENANGGALAN2*\n_Kecamatan Penanggalan Dalam Angka Tahun 2017_\n\
✅ *PENANGGALAN3*\n_Kecamatan Penanggalan Dalam Angka Tahun 2018_\n\
✅ *PENANGGALAN4*\n_Kecamatan Penanggalan Dalam Angka Tahun 2019_\n\
✅ *PENANGGALAN5*\n_Kecamatan Penanggalan Dalam Angka Tahun 2020_\n\n\
Silahkan masukan *Kode Publikasi* 📕 untuk menampilkan Publikasi yang Anda inginkan.\nContoh : *PENANGGALAN1* atau ketik *Menu* untuk kembali ke menu utama'
    return penanggalan

def rundeng():
    rundeng='*PUBLIKASI KECAMATAN RUNDENG DALAM ANGKA* 📕\n\n\
Silahkan pilih publikasi yang ingin ditampilkan\n\n\
✅ *RUNDENG1*\n_Kecamatan Rundeng Dalam Angka Tahun 2016_\n\
✅ *RUNDENG2*\n_Kecamatan Rundeng Dalam Angka Tahun 2017_\n\
✅ *RUNDENG3*\n_Kecamatan Rundeng Dalam Angka Tahun 2018_\n\
✅ *RUNDENG4*\n_Kecamatan Rundeng Dalam Angka Tahun 2019_\n\
✅ *RUNDENG5*\n_Kecamatan Rundeng Dalam Angka Tahun 2020_\n\n\
Silahkan masukan *Kode Publikasi* 📕 untuk menampilkan Publikasi yang Anda inginkan.\nContoh : *RUNDENG1* atau ketik *Menu* untuk kembali ke menu utama'
    return rundeng

def sultan():
    sultan='*PUBLIKASI KECAMATAN SULTAN DAULAT DALAM ANGKA* 📕\n\n\
Silahkan pilih publikasi yang ingin ditampilkan\n\n\
✅ *SULTANDAULAT1*\n_Kecamatan Sultan Daulat Dalam Angka Tahun 2016_\n\
✅ *SULTANDAULAT2*\n_Kecamatan Sultan Daulat Dalam Angka Tahun 2017_\n\
✅ *SULTANDAULAT3*\n_Kecamatan Sultan Daulat Dalam Angka Tahun 2018_\n\
✅ *SULTANDAULAT4*\n_Kecamatan Sultan Daulat Dalam Angka Tahun 2019_\n\
✅ *SULTANDAULAT5*\n_Kecamatan Sultan Daulat Dalam Angka Tahun 2020_\n\n\
Silahkan masukan *Kode Publikasi* 📕 untuk menampilkan Publikasi yang Anda inginkan.\nContoh : *SULTANDAULAT1* atau ketik *Menu* untuk kembali ke menu utama'
    return sultan

def longkib():
    longkib='*PUBLIKASI KECAMATAN LONGKIB DALAM ANGKA* 📕\n\n\
Silahkan pilih publikasi yang ingin ditampilkan\n\n\
✅ *LONGKIB1*\n_Kecamatan Longkib Dalam Angka Tahun 2016_\n\
✅ *LONGKIB2*\n_Kecamatan Longkib Dalam Angka Tahun 2017_\n\
✅ *LONGKIB3*\n_Kecamatan Longkib Dalam Angka Tahun 2018_\n\
✅ *LONGKIB4*\n_Kecamatan Longkib Dalam Angka Tahun 2019_\n\
✅ *LONGKIB5*\n_Kecamatan Longkib Dalam Angka Tahun 2020_\n\n\
Silahkan masukan *Kode Publikasi* 📕 untuk menampilkan Publikasi yang Anda inginkan.\nContoh : *LONGKIB1* atau ketik *Menu* untuk kembali ke menu utama'
    return longkib

def pdrb():
    pdrb='*PUBLIKASI STATISTIK* 📙 \n*PDRB MENURUT LAPANGAN USAHA KOTA SUBULUSSALAM* 📈\n\n\
Silahkan pilih publikasi yang ingin ditampilkan\n\n\
✅ *PDRB1*\n_Produk Domestik Regional Bruto Menurut Lapangan Usaha Kota Subulussalam Tahun 2011-2015_\n\
✅ *PDRB2*\n_Produk Domestik Regional Bruto Menurut Lapangan Usaha Kota Subulussalam Tahun 2013-2017_\n\
✅ *PDRB3*\n_Produk Domestik Regional Bruto Menurut Lapangan Usaha Kota Subulussalam Tahun 2014-2018_\n\
✅ *PDRB4*\n_Produk Domestik Regional Bruto Menurut Lapangan Usaha Kota Subulussalam Tahun 2015-2019_\n\
✅ *PDRB5*\n_Produk Domestik Regional Bruto Menurut Lapangan Usaha Kota Subulussalam Tahun 2016-2020_\n\n\
Silahkan masukan *Kode Publikasi* 📙 untuk menampilkan Publikasi yang Anda inginkan.\nContoh : *PDRB1* atau ketik *Menu* untuk kembali ke menu utama'
    return pdrb

def layanan():
   layanan='*Layanan di BPS Kota Subulussalam* 🏢\n\n\
✅ *Layanan Konsultasi Statistik di Kantor BPS*\n\
Hari Layanan  : Senin-Jumat \n_(kecuali hari libur)_\n\
Jam Layanan  : 08.00-15.00 WIB\n\n\
✅ *Layanan Konsultasi Statistik Online*\n\
Anda dapat melakukan konsultasi statistik secara online melalui media Whatsapp chat ataupun email dengan menghubungi petugas kami melalui tautan dibawah ini :\n📱 https://wa.me/6282210555432 \natau melalui email\n📧 bps1175@bps.go.id\n\n\
Hari Layanan  : Senin-Jumat \n_(kecuali hari libur)_\n\
Jam Layanan  : 09.00-14.00 WIB \n\n\
Untuk kembali ke menu utama silahkan ketik *Menu*'
   return layanan

def tentang():
    tentang='🎯 *Visi* _Badan Pusat Statistik Kota Subulussalam_ adalah sebagai :\n\n\
✨ _*Penyedia Data Statistik Berkualitas untuk Indonesia*_ ✨\n\n\
Dalam 🎯 *Visi* tersebut BPS bertekad untuk menghasilkan statistik _Nasional_ maupun _Internasional_ yang akurat dan terpercaya \
untuk mendukung Indonesia Maju. 🚀\n\n\
Bagi Pengguna Data yang ingin mendapatkan data BPS secara lengkap.\nAnda dapat mengunjungi website kami di:\n\n\
subulussalamkota.bps.go.id 🌐\n\n\
Atau follow akun Instagram kami di\n\n\
https://instagram.com/bps.subulussalam 📌 \n\n\
Untuk kembali ke menu utama silahkan ketik *Menu*'
    return tentang

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)