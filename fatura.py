#! /usr/bin/env python
# -*- coding: UTF-8 -*-
class fatura:
    indirim_durumu = ""
    indirim_list = ['Y', 'y', 'S', 's', 'G', 'g', 'E', 'e']
    abone_varmi = "E"
    abone_sayisi = 0
    konut_hane_sayisi_toplam = 0
    isyeri_abone_sayisi = 0
    resmi_daire_abone_sayisi = 0
    organize_sanayi_abone_sayisi = 0
    tarim_hayvan_sulama_abone_sayisi = 0
    konut_hane_su_tuketim_miktari = 0
    konut_hane_sayisi_kademe1_toplam = 0
    konut_hane_sayisi_kademe2_toplam = 0
    konut_hane_sayisi_kademe3_toplam = 0
    konut_hane_su_tuketim_miktari_kademe1 = 0
    konut_hane_su_tuketim_miktari_kademe2 = 0
    konut_hane_su_tuketim_miktari_kademe3 = 0
    tarimsal_50den_fazla = 0  # Aylik su tuketim miktari 50 tondan fazla olan ilce tarimsal ve hayvan sulama tipi abonelerin sayisi
    aylik_100ton_veya_500tl = 0  # Aylik su tuketim miktari 100 tondan yuksek veya aylik su tuketim ucreti 500 TLíden yuksek olan abonelerin (hanelerin) sayisi
    indirimli_hane_sayisi = 0
    engelli_hane_sayisi = 0
    resmi_daire_su_tuketim_max = 0
    resmi_daire_abone_no_max = 0
    su_tuketim_ucreti_max = 0
    su_tuketim_ucreti_max_abone_no = 0
    su_tuketim_ucreti_max_miktari = 0
    su_tuketim_miktari_toplam = 0
    resmi_daire_su_tuketim = 0
    isyeri_su_tuketim = 0
    organize_sanayi_su_tuketim = 0
    tarim_hayvan_su_tuketim = 0
    konut_hane_su_ucreti = 0
    isyeri_su_ucreti = 0
    resmi_daire_su_ucreti = 0
    organize_sanayi_su_ucreti = 0
    tarim_hayvan_su_ucreti = 0

    izsu_payi_toplam = 0
    ilce_payi_toplam = 0
    buyuksehir_payi = 0
    devlet_payi = 0
    abone_tipi_adi_max = ""

    def calculte(self):
        while (self.abone_varmi == "E" or self.abone_varmi == "e"):
            self.abone_sayisi += 1
            abone_no = int(input("Abone numaranizi giriniz: "))
            print("***************************")
            print("(1)Konut \n(2)isyeri \n(3)Resmi Daire \n(4)Organize Sanayi \n(5)ilce Tarimsal ve Hayvan Sulama")
            print("***************************")
            while True:
                abone_tipi_kodu = int(input("Abone tipi kodunu giriniz: "))
                if (abone_tipi_kodu > 5 and abone_tipi_kodu < 1):
                    print("Hatali kod girdiniz!")
                else:
                    break
            if (abone_tipi_kodu == 1):
                while True:
                    hane_sayisi = int(input("Hane sayisini giriniz:"))
                    hane_sayisi_temp = hane_sayisi
                    if (hane_sayisi < 1):
                        print("Hatali sayi girdiniz!")
                    else:
                        break
                if (hane_sayisi == 1):
                    while True:
                        self.indirim_durumu = input(
                            "indirim durumunuzu giriniz: (Yok | sehit | Gazi | Sporcu | Engelli: (Y|y|s|s|G|g|S|s|E|e karakterleri))")

                        if ((self.indirim_durumu) not in (self.indirim_list)):
                            print("Hatali girdi verdiniz!")
                        else:
                            break

                if (hane_sayisi > 1):
                    while True:
                        indirimli_sayisi = int(input("sehit, gazi veya sporcu olan abone sayisi(Yoksa 0)"))
                        engelli_sayisi = int(input("Engelli abone sayisi"))
                        if (indirimli_sayisi < 0 or engelli_sayisi < 0):
                            print("Hatali sayi girdiniz!")
                            continue
                        if (indirimli_sayisi + engelli_sayisi > hane_sayisi):
                            print("Fazla deger girdiniz! Lutfen tekrar giriniz.")
                        else:
                            break
                while True:
                    onceki_sayac = float(input("onceki sayac degerini giriniz: "))
                    if (onceki_sayac < 0):
                        print("Hatali veri girisi!")
                        continue
                    simdiki_sayac = float(input("simdiki sayac degerini giriniz: "))
                    while (simdiki_sayac < onceki_sayac):
                        print("Hatali veri girisi!")
                        simdiki_sayac = float(input("simdiki sayac degerini giriniz: "))
                    sayac_gun_sayisi = int(
                        input("onceki ve simdiki sayac okuma tarihleri arasindaki gun sayisini giriniz: "))
                    while (sayac_gun_sayisi <= 0):
                        print("Hatali veri girisi!")
                        sayac_gun_sayisi = int(
                            input("onceki ve simdiki sayac okuma tarihleri arasindaki gun sayisini giriniz: "))
                    else:
                        break
                oran_kademe1 = sayac_gun_sayisi * 13 / 30
                oran_kademe2 = sayac_gun_sayisi * 20 / 30
            if (abone_tipi_kodu == 1):
                if (hane_sayisi == 1):
                    self.konut_hane_sayisi_toplam += 1
                    print("Abone no: ", abone_no)
                    print("Abone tipi adi: Konut")
                    donemlik_su_miktari = simdiki_sayac - onceki_sayac
                    self.konut_hane_su_tuketim_miktari += donemlik_su_miktari / sayac_gun_sayisi * 30
                    if (
                            self.indirim_durumu == "E" or self.indirim_durumu == "e"):  # ENGELLI INDIRIMI DoNEMLIK SU uCRETI VE DoNEMLIK ATIK SU uCRETINDEN KESILMIsTIR!
                        self.engelli_hane_sayisi += 1
                        if (donemlik_su_miktari <= oran_kademe1):
                            donemlik_su_ucreti = (donemlik_su_miktari * 2.89) / 2
                            self.konut_hane_sayisi_kademe1_toplam += 1
                            self.konut_hane_su_tuketim_miktari_kademe1 += donemlik_su_miktari / sayac_gun_sayisi * 30
                            self.konut_hane_su_ucreti += donemlik_su_ucreti / sayac_gun_sayisi * 30
                        elif (donemlik_su_miktari <= oran_kademe2):
                            donemlik_su_ucreti = (oran_kademe1 * 2.89 + (donemlik_su_miktari - oran_kademe1) * 3.13) / 2
                            self.konut_hane_sayisi_kademe2_toplam += 1
                            self.konut_hane_su_tuketim_miktari_kademe2 += donemlik_su_miktari / sayac_gun_sayisi * 30
                            self.konut_hane_su_ucreti += donemlik_su_ucreti / sayac_gun_sayisi * 30
                        else:
                            donemlik_su_ucreti = (oran_kademe1 * 2.89 + (oran_kademe2 - oran_kademe1) * 3.13) / 2 + (
                                    (donemlik_su_miktari - oran_kademe2) * 6.43)
                            self.konut_hane_sayisi_kademe3_toplam += 1
                            self.konut_hane_su_tuketim_miktari_kademe3 += donemlik_su_miktari / sayac_gun_sayisi * 30
                            self.konut_hane_su_ucreti += donemlik_su_ucreti / sayac_gun_sayisi * 30
                        self.su_tuketim_miktari_toplam += donemlik_su_miktari / sayac_gun_sayisi * 30
                        if (donemlik_su_miktari <= oran_kademe1):
                            donemlik_atik_su_ucreti = (donemlik_su_miktari * 1.44) / 2
                        elif (donemlik_su_miktari <= oran_kademe2):
                            donemlik_atik_su_ucreti = (oran_kademe1 * 1.44 + (
                                    donemlik_su_miktari - oran_kademe1) * 1.56) / 2
                        else:
                            donemlik_atik_su_ucreti = (oran_kademe1 * 1.44 + (
                                    oran_kademe2 - oran_kademe1) * 1.56) / 2 + (
                                                                  donemlik_su_miktari - oran_kademe2) * 3.22
                        if (
                                donemlik_su_miktari / sayac_gun_sayisi * 30 > 100 or donemlik_su_ucreti / sayac_gun_sayisi * 30 > 500):
                            self.aylik_100ton_veya_500tl += 1
                        print("Donemlik su tuketim miktari: ", format(donemlik_su_miktari, ".2f"), "ton")
                        print("Donemlik su tuketim ucreti: ", format(donemlik_su_ucreti, ".2f"), "TL")
                        print("Donemlik atik su tuketim ucreti: ", format(donemlik_atik_su_ucreti, ".2f"), "TL")
                        print("Donemlik toplam su tuketim ve atik su ucreti :",
                              format(donemlik_su_ucreti + donemlik_atik_su_ucreti, ".2f"), "TL")
                        print("Donemlik cTV tutari: ", format(donemlik_su_miktari * 0.39, ".2f"), "TL")
                        print("Donemlik kati atik toplama ucreti: ", 13, "TL")
                        print("Donemlik kati atik bertaraf ucreti: ", 2.54, "TL")
                        donemlik_toplam_fatura = donemlik_su_ucreti + donemlik_atik_su_ucreti + donemlik_su_miktari * 0.39 + 13 + 2.54 + \
                                                 (donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100
                        print("Donemlik toplam fatura :", format(donemlik_toplam_fatura, ".2f"), "TL")
                        print("Donemlik devlete aktarilacak KDV tutari(%8): ",
                              format((donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100, ".2f"), "TL")
                        print("Donemlik ilce belediyesine aktarilacak tutar: ",
                              format(donemlik_su_miktari * 0.39 + 13, ".2f"), "TL")
                        print("Donemlik buyuksehir belediyesine aktarilacak tutar: ", 2.54, "TL")
                        print("Donemlik iZSU payi: ", format(donemlik_toplam_fatura - (
                                ((donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100) + (
                                donemlik_su_miktari * 0.39 + 13) + 2.54), ".2f"), "TL")
                        self.devlet_payi += (donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100
                        self.ilce_payi_toplam += donemlik_su_miktari * 0.39 + 13
                        self.buyuksehir_payi += 2.54
                        self.izsu_payi_toplam += donemlik_toplam_fatura - (
                                ((donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100) + (
                                donemlik_su_miktari * 0.39 + 13) + 2.54)
                    elif (
                            self.indirim_durumu != "Y" or self.indirim_durumu != "y"):  # iNDIRIM DoNEMLIK SU uCRETI VE DoNEMLIK ATIK SU uCRETINDEN KESILMIsTIR!
                        self.indirimli_hane_sayisi += 1
                        if (donemlik_su_miktari <= oran_kademe1):
                            donemlik_su_ucreti = (donemlik_su_miktari * 2.89) / 2
                            self.konut_hane_sayisi_kademe1_toplam += 1
                            self.konut_hane_su_ucreti += donemlik_su_ucreti / sayac_gun_sayisi * 30
                            self.konut_hane_su_tuketim_miktari_kademe1 += donemlik_su_miktari / sayac_gun_sayisi * 30
                        elif (donemlik_su_miktari <= oran_kademe2):
                            donemlik_su_ucreti = (oran_kademe1 * 2.89 + (donemlik_su_miktari - oran_kademe1) * 3.13) / 2
                            self.konut_hane_sayisi_kademe2_toplam += 1
                            self.konut_hane_su_tuketim_miktari_kademe2 += donemlik_su_miktari / sayac_gun_sayisi * 30
                            self.konut_hane_su_ucreti += donemlik_su_ucreti / sayac_gun_sayisi * 30
                        else:
                            donemlik_su_ucreti = (oran_kademe1 * 2.89 + (oran_kademe2 - oran_kademe1) * 3.13 + (
                                    (donemlik_su_miktari - oran_kademe2) * 6.43)) / 2
                            self.konut_hane_sayisi_kademe3_toplam += 1
                            self.konut_hane_su_tuketim_miktari_kademe3 += donemlik_su_miktari / sayac_gun_sayisi * 30
                            self.konut_hane_su_ucreti += donemlik_su_ucreti / sayac_gun_sayisi * 30
                        self.su_tuketim_miktari_toplam += donemlik_su_miktari / sayac_gun_sayisi * 30
                        if (donemlik_su_miktari <= oran_kademe1):
                            donemlik_atik_su_ucreti = (donemlik_su_miktari * 1.44) / 2
                        elif (donemlik_su_miktari <= oran_kademe2):
                            donemlik_atik_su_ucreti = (oran_kademe1 * 1.44 + (
                                    donemlik_su_miktari - oran_kademe1) * 1.56) / 2
                        else:
                            donemlik_atik_su_ucreti = (oran_kademe1 * 1.44 + (oran_kademe2 - oran_kademe1) * 1.56 + (
                                    donemlik_su_miktari - oran_kademe2) * 3.22) / 2
                        if (
                                donemlik_su_miktari / sayac_gun_sayisi * 30 > 100 or donemlik_su_ucreti / sayac_gun_sayisi * 30 > 500):
                            self.aylik_100ton_veya_500tl += 1
                        print("Donemlik su tuketim miktari: ", format(donemlik_su_miktari, ".2f"), "ton")
                        print("Donemlik su tuketim ucreti: ", format(donemlik_su_ucreti, ".2f"), "TL")
                        print("Donemlik atik su tuketim ucreti: ", format(donemlik_atik_su_ucreti, ".2f"), "TL")
                        print("Donemlik toplam su tuketim ve atik su ucreti :",
                              format(donemlik_su_ucreti + donemlik_atik_su_ucreti, ".2f"), "TL")
                        print("Donemlik cTV tutari: ", format(donemlik_su_miktari * 0.39, ".2f"), "TL")
                        print("Donemlik kati atik toplama ucreti: ", 13, "TL")
                        print("Donemlik kati atik bertaraf ucreti: ", 2.54, "TL")
                        donemlik_toplam_fatura = donemlik_su_ucreti + donemlik_atik_su_ucreti + donemlik_su_miktari * 0.39 + 13 + 2.54 + \
                                                 (donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100
                        print("Donemlik toplam fatura :", format(donemlik_toplam_fatura, ".2f"), "TL")
                        print("Donemlik devlete aktarilacak KDV tutari(%8): ",
                              format((donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100, ".2f"), "TL")
                        print("Donemlik ilce belediyesine aktarilacak tutar: ",
                              format(donemlik_su_miktari * 0.39 + 13, ".2f"), "TL")
                        print("Donemlik buyuksehir belediyesine aktarilacak tutar: ", 2.54, "TL")
                        print("Donemlik iZSU payi: ", format(donemlik_toplam_fatura - (
                                ((donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100) + (
                                donemlik_su_miktari * 0.39 + 13) + 2.54), ".2f"), "TL")
                        self.devlet_payi += (donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100
                        self.ilce_payi_toplam += donemlik_su_miktari * 0.39 + 13
                        self.buyuksehir_payi += 2.54
                        self.izsu_payi_toplam += donemlik_toplam_fatura - (
                                ((donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100) + (
                                donemlik_su_miktari * 0.39 + 13) + 2.54)
                    else:
                        if (donemlik_su_miktari <= oran_kademe1):
                            donemlik_su_ucreti = (donemlik_su_miktari * 2.89)
                            self.konut_hane_sayisi_kademe1_toplam += 1
                            self.konut_hane_su_ucreti += donemlik_su_ucreti / sayac_gun_sayisi * 30
                            self.konut_hane_su_tuketim_miktari_kademe1 += donemlik_su_miktari / sayac_gun_sayisi * 30
                        elif (donemlik_su_miktari <= oran_kademe2):
                            donemlik_su_ucreti = (oran_kademe1 * 2.89 + (donemlik_su_miktari - oran_kademe1) * 3.13)
                            self.konut_hane_sayisi_kademe2_toplam += 1
                            self.konut_hane_su_ucreti += donemlik_su_ucreti / sayac_gun_sayisi * 30
                            self.konut_hane_su_tuketim_miktari_kademe2 += donemlik_su_miktari / sayac_gun_sayisi * 30
                        else:
                            donemlik_su_ucreti = (oran_kademe1 * 2.89 + (oran_kademe2 - oran_kademe1) * 3.13 + (
                                    donemlik_su_miktari - oran_kademe2 * 6.43))
                            self.konut_hane_sayisi_kademe3_toplam += 1
                            self.konut_hane_su_ucreti += donemlik_su_ucreti / sayac_gun_sayisi * 30
                            self.konut_hane_su_tuketim_miktari_kademe3 += donemlik_su_miktari / sayac_gun_sayisi * 30
                        self.su_tuketim_miktari_toplam += donemlik_su_miktari / sayac_gun_sayisi * 30
                        if (donemlik_su_miktari <= oran_kademe1):
                            donemlik_atik_su_ucreti = (donemlik_su_miktari * 1.44)
                        elif (donemlik_su_miktari <= oran_kademe2):
                            donemlik_atik_su_ucreti = (
                                    oran_kademe1 * 1.44 + (donemlik_su_miktari - oran_kademe2) * 1.56)
                        else:
                            donemlik_atik_su_ucreti = (oran_kademe1 * 1.44 + (oran_kademe2 - oran_kademe1) * 1.56 + (
                                    donemlik_su_miktari - oran_kademe2) * 3.22)
                        if (
                                donemlik_su_miktari / sayac_gun_sayisi * 30 > 100 or donemlik_su_ucreti / sayac_gun_sayisi * 30 > 500):
                            self.aylik_100ton_veya_500tl += 1
                        print("Donemlik su tuketim miktari: ", format(donemlik_su_miktari, ".2f"), "ton")
                        print("Donemlik su tuketim ucreti: ", format(donemlik_su_ucreti, ".2f"), "TL")
                        print("Donemlik atik su tuketim ucreti: ", format(donemlik_atik_su_ucreti, ".2f"), "TL")
                        print("Donemlik toplam su tuketim ve atik su ucreti :",
                              format(donemlik_su_ucreti + donemlik_atik_su_ucreti, ".2f"), "TL")
                        print("Donemlik cTV tutari: ", format(donemlik_su_miktari * 0.39, ".2f"), "TL")
                        print("Donemlik kati atik toplama ucreti: ", 13, "TL")
                        print("Donemlik kati atik bertaraf ucreti: ", 2.54, "TL")
                        donemlik_toplam_fatura = donemlik_su_ucreti + donemlik_atik_su_ucreti + donemlik_su_miktari * 0.39 + 13 + 2.54 + \
                                                 (donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100
                        print("Donemlik toplam fatura :", format(donemlik_toplam_fatura, ".2f"), "TL")
                        print("Donemlik devlete aktarilacak KDV tutari(%8): ",
                              format((donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100, ".2f"), "TL")
                        print("Donemlik ilce belediyesine aktarilacak tutar: ",
                              format(donemlik_su_miktari * 0.39 + 13, ".2f"), "TL")
                        print("Donemlik buyuksehir belediyesine aktarilacak tutar: ", 2.54, "TL")
                        print("Donemlik iZSU payi: ", format(donemlik_toplam_fatura - (
                                ((donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100) + (
                                donemlik_su_miktari * 0.39 + 13) + 2.54), ".2f"), "TL")
                        self.devlet_payi += (donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100
                        self.ilce_payi_toplam += donemlik_su_miktari * 0.39 + 13
                        self.buyuksehir_payi += 2.54
                        self.izsu_payi_toplam += donemlik_toplam_fatura - (
                                ((donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100) + (
                                donemlik_su_miktari * 0.39 + 13) + 2.54)

                else:
                    sayi = 0
                    donemlik_su_miktari_toplam = simdiki_sayac - onceki_sayac;
                    donemlik_su_ucreti_toplam = 0;
                    donemlik_atik_su_ucreti_toplam = 0
                    donemlik_toplam_su_atik_su_ucreti_toplam = 0;
                    donemlik_ctv_tutari = 0;
                    donemlik_kati_atik_toplam = 0;
                    donemlik_kati_atik_bertaraf_toplam = 0
                    donemlik_fatura_toplam = 0;
                    donemlik_kdv_toplam = 0;
                    donemlik_ilce = 0;
                    donemlik_buyuksehir = 0;
                    donemlik_izsu = 0
                    while (sayi < indirimli_sayisi):
                        self.konut_hane_sayisi_toplam += 1
                        self.indirimli_hane_sayisi += 1
                        sayi += 1
                        hane_sayisi_temp -= 1
                        donemlik_su_miktari = (simdiki_sayac - onceki_sayac) / hane_sayisi
                        self.konut_hane_su_tuketim_miktari += donemlik_su_miktari / sayac_gun_sayisi * 30
                        self.su_tuketim_miktari_toplam += donemlik_su_miktari / sayac_gun_sayisi * 30
                        if (donemlik_su_miktari <= oran_kademe1):
                            donemlik_su_ucreti = (donemlik_su_miktari * 2.89)
                            self.konut_hane_su_ucreti += donemlik_su_ucreti / sayac_gun_sayisi * 30
                            donemlik_su_ucreti_toplam += donemlik_su_ucreti
                            self.konut_hane_sayisi_kademe1_toplam += 1
                            self.konut_hane_su_tuketim_miktari_kademe1 += donemlik_su_miktari / sayac_gun_sayisi * 30
                        elif (donemlik_su_miktari <= oran_kademe2):
                            donemlik_su_ucreti = (oran_kademe1 * 2.89 + (donemlik_su_miktari - oran_kademe1) * 3.13)
                            donemlik_su_ucreti_toplam += donemlik_su_ucreti
                            self.konut_hane_sayisi_kademe2_toplam += 1
                            self.konut_hane_su_ucreti += donemlik_su_ucreti / sayac_gun_sayisi * 30
                            self.konut_hane_su_tuketim_miktari_kademe2 += donemlik_su_miktari / sayac_gun_sayisi * 30
                        else:
                            donemlik_su_ucreti = (oran_kademe1 * 2.89 + (oran_kademe2 - oran_kademe1) * 3.13 + (
                                    (donemlik_su_miktari - oran_kademe2) * 6.43))
                            donemlik_su_ucreti_toplam += donemlik_su_ucreti
                            self.konut_hane_su_ucreti += donemlik_su_ucreti / sayac_gun_sayisi * 30
                            self.konut_hane_sayisi_kademe3_toplam += 1
                            self.konut_hane_su_tuketim_miktari_kademe3 += donemlik_su_miktari / sayac_gun_sayisi * 30
                        if (donemlik_su_miktari <= oran_kademe1):
                            donemlik_atik_su_ucreti = (donemlik_su_miktari * 1.44)
                            donemlik_atik_su_ucreti_toplam += donemlik_atik_su_ucreti
                        elif (donemlik_su_miktari <= oran_kademe2):
                            donemlik_atik_su_ucreti = (
                                    oran_kademe1 * 1.44 + (donemlik_su_miktari - oran_kademe1) * 1.56)
                            donemlik_atik_su_ucreti_toplam += donemlik_atik_su_ucreti
                        else:
                            donemlik_atik_su_ucreti = (oran_kademe1 * 1.44 + (oran_kademe2 - oran_kademe1) * 1.56 + (
                                    donemlik_su_miktari - oran_kademe2) * 3.22)
                            donemlik_atik_su_ucreti_toplam += donemlik_atik_su_ucreti
                        if (
                                donemlik_su_miktari / sayac_gun_sayisi * 30 > 100 or donemlik_su_ucreti / sayac_gun_sayisi * 30 > 500):
                            self.aylik_100ton_veya_500tl += 1
                        donemlik_toplam_su_atik_su_ucreti = donemlik_su_ucreti + donemlik_atik_su_ucreti
                        donemlik_toplam_su_atik_su_ucreti_toplam += donemlik_toplam_su_atik_su_ucreti
                        donemlik_ctv_tutari += donemlik_su_miktari * 0.39
                        donemlik_kati_atik_toplam += 13
                        donemlik_kati_atik_bertaraf_toplam = 2.54
                        donemlik_toplam_fatura = donemlik_su_ucreti + donemlik_atik_su_ucreti + (
                                donemlik_su_miktari * 0.39) + 13 + 2.54 + \
                                                 (donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100
                        donemlik_fatura_toplam += donemlik_toplam_fatura
                        donemlik_kdv_toplam += (donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100
                        donemlik_ilce += donemlik_su_miktari * 0.39 + 13
                        donemlik_buyuksehir += 2.54
                        donemlik_izsu += donemlik_toplam_fatura - (
                                ((donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100) + (
                                donemlik_su_miktari * 0.39 + 13) + 2.54)
                    sayi = 0
                    while (sayi < engelli_sayisi):
                        self.konut_hane_sayisi_toplam += 1
                        self.engelli_hane_sayisi += 1
                        sayi += 1
                        hane_sayisi_temp -= 1
                        donemlik_su_miktari = (simdiki_sayac - onceki_sayac) / hane_sayisi
                        self.konut_hane_su_tuketim_miktari += donemlik_su_miktari / sayac_gun_sayisi * 30
                        self.su_tuketim_miktari_toplam += donemlik_su_miktari / sayac_gun_sayisi * 30
                        if (donemlik_su_miktari <= oran_kademe1):
                            donemlik_su_ucreti = (donemlik_su_miktari * 2.89) / 2
                            self.konut_hane_su_ucreti += donemlik_su_ucreti / sayac_gun_sayisi * 30
                            donemlik_su_ucreti_toplam += donemlik_su_ucreti
                            self.konut_hane_sayisi_kademe1_toplam += 1
                            self.konut_hane_su_tuketim_miktari_kademe1 += donemlik_su_miktari / sayac_gun_sayisi * 30
                        elif (donemlik_su_miktari <= oran_kademe2):
                            donemlik_su_ucreti = (oran_kademe1 * 2.89 + (donemlik_su_miktari - oran_kademe1) * 3.13) / 2
                            donemlik_su_ucreti_toplam += donemlik_su_ucreti
                            self.konut_hane_sayisi_kademe2_toplam += 1
                            self.konut_hane_su_ucreti += donemlik_su_ucreti / sayac_gun_sayisi * 30
                            self.konut_hane_su_tuketim_miktari_kademe2 += donemlik_su_miktari / sayac_gun_sayisi * 30
                        else:
                            donemlik_su_ucreti = (oran_kademe1 * 2.89 + (oran_kademe2 - oran_kademe1) * 3.13) / 2 + (
                                    donemlik_su_miktari - oran_kademe2 * 6.43)
                            donemlik_su_ucreti_toplam += donemlik_su_ucreti
                            self.konut_hane_sayisi_kademe3_toplam += 1
                            self.konut_hane_su_ucreti += donemlik_su_ucreti / sayac_gun_sayisi * 30
                            self.konut_hane_su_tuketim_miktari_kademe3 += donemlik_su_miktari / sayac_gun_sayisi * 30
                        if (donemlik_su_miktari <= oran_kademe1):
                            donemlik_atik_su_ucreti = (donemlik_su_miktari * 1.44) / 2
                            donemlik_atik_su_ucreti_toplam += donemlik_atik_su_ucreti
                        elif (donemlik_su_miktari <= oran_kademe2):
                            donemlik_atik_su_ucreti = (oran_kademe1 * 1.44 + (
                                    donemlik_su_miktari - oran_kademe1) * 1.56) / 2
                            donemlik_atik_su_ucreti_toplam += donemlik_atik_su_ucreti
                        else:
                            donemlik_atik_su_ucreti = (oran_kademe1 * 1.44 + (
                                    oran_kademe2 - oran_kademe1) * 1.56) / 2 + (
                                                                  donemlik_su_miktari - oran_kademe2) * 3.22
                            donemlik_atik_su_ucreti_toplam += donemlik_atik_su_ucreti
                        if (
                                donemlik_su_miktari / sayac_gun_sayisi * 30 > 100 or donemlik_su_ucreti / sayac_gun_sayisi * 30 > 500):
                            self.aylik_100ton_veya_500tl += 1
                        donemlik_toplam_su_atik_su_ucreti = donemlik_su_ucreti + donemlik_atik_su_ucreti
                        donemlik_toplam_su_atik_su_ucreti_toplam += donemlik_toplam_su_atik_su_ucreti
                        donemlik_ctv_tutari += donemlik_su_miktari * 0.39
                        donemlik_kati_atik_toplam += 13
                        donemlik_kati_atik_bertaraf_toplam += 2.54
                        donemlik_toplam_fatura = donemlik_su_ucreti + donemlik_atik_su_ucreti + (
                                donemlik_su_miktari * 0.39) + 13 + 2.54 + \
                                                 (donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100
                        donemlik_fatura_toplam += donemlik_toplam_fatura
                        donemlik_kdv_toplam += (donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100
                        donemlik_ilce += donemlik_su_miktari * 0.39 + 13
                        donemlik_buyuksehir += 2.54
                        donemlik_izsu += donemlik_toplam_fatura - (
                                ((donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100) + (
                                donemlik_su_miktari * 0.39 + 13) + 2.54)
                    sayi = 0
                    while (sayi < hane_sayisi_temp):
                        self.konut_hane_sayisi_toplam += 1
                        sayi += 1
                        donemlik_su_miktari = (simdiki_sayac - onceki_sayac) / hane_sayisi
                        self.konut_hane_su_tuketim_miktari += donemlik_su_miktari / sayac_gun_sayisi * 30
                        self.su_tuketim_miktari_toplam += donemlik_su_miktari / sayac_gun_sayisi * 30
                        if (donemlik_su_miktari <= oran_kademe1):
                            donemlik_su_ucreti = (donemlik_su_miktari * 2.89)
                            donemlik_su_ucreti_toplam += donemlik_su_ucreti
                            self.konut_hane_sayisi_kademe1_toplam += 1
                            self.konut_hane_su_ucreti += donemlik_su_ucreti / sayac_gun_sayisi * 30
                            self.konut_hane_su_tuketim_miktari_kademe1 += donemlik_su_miktari / sayac_gun_sayisi * 30
                        elif (donemlik_su_miktari <= oran_kademe2):
                            donemlik_su_ucreti = (oran_kademe1 * 2.89 + (donemlik_su_miktari - oran_kademe1) * 3.13)
                            donemlik_su_ucreti_toplam += donemlik_su_ucreti
                            self.konut_hane_su_ucreti += donemlik_su_ucreti / sayac_gun_sayisi * 30
                            self.konut_hane_sayisi_kademe2_toplam += 1
                            self.konut_hane_su_tuketim_miktari_kademe2 += donemlik_su_miktari / sayac_gun_sayisi * 30
                        else:
                            donemlik_su_ucreti = (oran_kademe1 * 2.89 + (oran_kademe2 - oran_kademe2) * 3.13 + (
                                    donemlik_su_miktari - oran_kademe2 * 6.43))
                            donemlik_su_ucreti_toplam += donemlik_su_ucreti
                            self.konut_hane_sayisi_kademe3_toplam += 1
                            self.konut_hane_su_ucreti += donemlik_su_ucreti / sayac_gun_sayisi * 30
                            self.konut_hane_su_tuketim_miktari_kademe3 += donemlik_su_miktari / sayac_gun_sayisi * 30
                        if (donemlik_su_miktari <= oran_kademe1):
                            donemlik_atik_su_ucreti = (donemlik_su_miktari * 1.44)
                            donemlik_atik_su_ucreti_toplam += donemlik_atik_su_ucreti
                        elif (donemlik_su_miktari <= oran_kademe2):
                            donemlik_atik_su_ucreti = (
                                    oran_kademe1 * 1.44 + (donemlik_su_miktari - oran_kademe1) * 1.56)
                            donemlik_atik_su_ucreti_toplam += donemlik_atik_su_ucreti
                        else:
                            donemlik_atik_su_ucreti = (oran_kademe1 * 1.44 + (oran_kademe2 - oran_kademe1) * 1.56 + (
                                    donemlik_su_miktari - oran_kademe2) * 3.22)
                            donemlik_atik_su_ucreti_toplam += donemlik_atik_su_ucreti
                        if (
                                donemlik_su_miktari / sayac_gun_sayisi * 30 > 100 or donemlik_su_ucreti / sayac_gun_sayisi * 30 > 500):
                            self.aylik_100ton_veya_500tl += 1
                        donemlik_toplam_su_atik_su_ucreti = donemlik_su_ucreti + donemlik_atik_su_ucreti
                        donemlik_toplam_su_atik_su_ucreti_toplam += donemlik_toplam_su_atik_su_ucreti
                        donemlik_ctv_tutari += donemlik_su_miktari * 0.39
                        donemlik_kati_atik_toplam += 13
                        donemlik_kati_atik_bertaraf_toplam = 2.54
                        donemlik_toplam_fatura = donemlik_su_ucreti + donemlik_atik_su_ucreti + (
                                donemlik_su_miktari * 0.39) + 13 + 2.54 + \
                                                 (donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100
                        donemlik_fatura_toplam += donemlik_toplam_fatura
                        donemlik_kdv_toplam += (donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100
                        donemlik_ilce += donemlik_su_miktari * 0.39 + 13
                        donemlik_buyuksehir += 2.54
                        donemlik_izsu += donemlik_toplam_fatura - (
                                ((donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100) + (
                                donemlik_su_miktari * 0.39 + 13) + 2.54)
                    print("Abone no:", abone_no)
                    print("Abone tipi adi: Karisik Grup")
                    print("Donemlik su tuketim miktari: ", format(donemlik_su_miktari_toplam, ".2f"), "ton")
                    print("Donemlik su tuketim ucreti: ", format(donemlik_su_ucreti_toplam, ".2f"), "TL")
                    print("Donemlik atik su ucreti: ", format(donemlik_atik_su_ucreti_toplam, ".2f"), "TL")
                    print("Donemlik toplam su tuketim ve atik su ucreti",
                          format(donemlik_toplam_su_atik_su_ucreti_toplam, ".2f"), "TL")
                    print("Donemlik cTV tutari: ", format(donemlik_ctv_tutari, ".2f"), "TL")
                    print("Donemlik kati atik toplama ucreti: ", format(donemlik_kati_atik_toplam, ".2f"), "TL")
                    print(
                        "Donemlik kati atik bertaraf ucreti: ", format(donemlik_kati_atik_bertaraf_toplam, ".2f"), "TL")
                    print("Donemlik toplam fatura tutari: ", format(donemlik_fatura_toplam, ".2f"), "TL")
                    print("Donemlik devlete aktarilacak KDV tutari (%8): ", format(donemlik_kdv_toplam, ".2f"), "TL")
                    print("Donemlik ilce belediyesine aktarilacak tutar: ", format(donemlik_ilce, ".2f"), "TL")
                    print(
                        "Donemlik buyuksehir belediyesine aktarilacak tutar: ", format(donemlik_buyuksehir, ".2f"),
                        "TL")
                    print("Donemlik iZSU payi", format(donemlik_izsu, ".2f"), "TL")
                    self.devlet_payi += (donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100
                    self.ilce_payi_toplam += donemlik_su_miktari * 0.39 + 13
                    self.buyuksehir_payi += 2.54
                    self.izsu_payi_toplam += donemlik_toplam_fatura - (
                            ((donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100) + (
                            donemlik_su_miktari * 0.39 + 13) + 2.54)
            elif (abone_tipi_kodu == 2):
                self.isyeri_abone_sayisi += 1
                while True:
                    onceki_sayac = float(input("onceki sayac degerini giriniz: "))
                    if (onceki_sayac < 0):
                        print("Hatali veri girisi!")
                        continue
                    simdiki_sayac = float(input("simdiki sayac degerini giriniz: "))
                    while (simdiki_sayac < onceki_sayac):
                        print("Hatali veri girisi!")
                        simdiki_sayac = float(input("simdiki sayac degerini giriniz: "))
                    sayac_gun_sayisi = int(
                        input("onceki ve simdiki sayac okuma tarihleri arasindaki gun sayisini giriniz: "))
                    while (sayac_gun_sayisi <= 0):
                        print("Hatali veri girisi!")
                        sayac_gun_sayisi = int(
                            input("onceki ve simdiki sayac okuma tarihleri arasindaki gun sayisini giriniz: "))
                    else:
                        break
                print("Abone no: ", abone_no)
                print("Abone tipi adi: isyeri")
                donemlik_su_miktari = simdiki_sayac - onceki_sayac
                self.isyeri_su_tuketim += donemlik_su_miktari / sayac_gun_sayisi * 30
                print("Donemlik su tuketim miktari: ", format(donemlik_su_miktari, ".2f"), "ton")
                self.su_tuketim_miktari_toplam += donemlik_su_miktari / sayac_gun_sayisi * 30
                donemlik_su_ucreti = donemlik_su_miktari * 7.38
                if (
                        donemlik_su_miktari / sayac_gun_sayisi * 30 > 100 or donemlik_su_ucreti / sayac_gun_sayisi * 30 > 500):
                    self.aylik_100ton_veya_500tl += 1
                print("Donemlik su tuketim ucreti: ", format(donemlik_su_ucreti, ".2f"), "TL")
                self.isyeri_su_ucreti += donemlik_su_ucreti / sayac_gun_sayisi * 30
                donemlik_atik_su_ucreti = donemlik_su_miktari * 3.68
                print("Donemlik toplam su tuketim ve atik su ucreti: ",
                      format(donemlik_atik_su_ucreti + donemlik_su_ucreti, ".2f"), "TL")
                print("Donemlik cTV tutari:", format(donemlik_su_miktari * 0.39, ".2f"), "TL")
                print("Donemlik kati atik toplama ucreti: ", 13, "TL")
                print("Donemlik kati atik bertaraf ucreti: ", 2.54, "TL")
                donemlik_toplam_fatura = donemlik_su_ucreti + donemlik_atik_su_ucreti + (
                        donemlik_su_miktari * 0.39) + 13 + 2.54 + \
                                         (donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100
                print("Donemlik toplam fatura tutari: ", format(donemlik_toplam_fatura, ".2f"), "TL")
                print("Donemlik devlete aktarilacak KDV tutari(%8): ",
                      format((donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100, ".2f"), "TL")
                print(
                    "Donemlik ilce belediyesine aktarilacak tutar: ", format(donemlik_su_miktari * 0.39 + 13, ".2f"),
                    "TL")
                print("Donemlik buyuksehir belediyesine aktarilacak tutar: ", 2.54, "TL")
                print("Donemlik iZSU payi: ", format(donemlik_toplam_fatura -
                                                     (((donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100) + (
                                                             donemlik_su_miktari * 0.39 + 13) + 2.54), ".2f"), "TL")
                self.devlet_payi += (donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100
                self.ilce_payi_toplam += donemlik_su_miktari * 0.39 + 13
                self.buyuksehir_payi += 2.54
                self.izsu_payi_toplam += donemlik_toplam_fatura - (
                        ((donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100) + (
                            donemlik_su_miktari * 0.39 + 13) + 2.54)
                if (donemlik_su_ucreti / sayac_gun_sayisi * 30 > self.su_tuketim_ucreti_max):
                    self.su_tuketim_ucreti_max = donemlik_su_ucreti / sayac_gun_sayisi * 30
                    self.abone_sayisi = abone_no
                    self.abone_tipi_adi_max = "isyeri"
                    self.su_tuketim_ucreti_max_miktari = donemlik_su_miktari / sayac_gun_sayisi * 30
            elif (abone_tipi_kodu == 3):
                self.resmi_daire_abone_sayisi += 1
                while True:
                    onceki_sayac = float(input("onceki sayac degerini giriniz: "))
                    if (onceki_sayac < 0):
                        print("Hatali veri girisi!")
                        continue
                    simdiki_sayac = float(input("simdiki sayac degerini giriniz: "))
                    while (simdiki_sayac < onceki_sayac):
                        print("Hatali veri girisi!")
                        simdiki_sayac = float(input("simdiki sayac degerini giriniz: "))
                    sayac_gun_sayisi = int(
                        input("onceki ve simdiki sayac okuma tarihleri arasindaki gun sayisini giriniz: "))
                    while (sayac_gun_sayisi <= 0):
                        print("Hatali veri girisi!")
                        sayac_gun_sayisi = int(
                            input("onceki ve simdiki sayac okuma tarihleri arasindaki gun sayisini giriniz: "))
                    else:
                        break
                print("Abone no: ", abone_no)
                print("Abone tipi adi: Resmi Daire")
                donemlik_su_miktari = simdiki_sayac - onceki_sayac
                print("Donemlik su tuketim miktari: ", format(donemlik_su_miktari, ".2f"), "ton")
                self.resmi_daire_su_tuketim += donemlik_su_miktari / sayac_gun_sayisi * 30
                self.su_tuketim_miktari_toplam += donemlik_su_miktari / sayac_gun_sayisi * 30
                donemlik_su_ucreti = donemlik_su_miktari * 4.34
                if (
                        donemlik_su_miktari / sayac_gun_sayisi * 30 > 100 or donemlik_su_ucreti / sayac_gun_sayisi * 30 > 500):
                    self.aylik_100ton_veya_500tl += 1
                print("Donemlik su tuketim ucreti: ", format(donemlik_su_ucreti, ".2f"), "TL")
                self.resmi_daire_su_ucreti += donemlik_su_ucreti / sayac_gun_sayisi * 30
                donemlik_atik_su_ucreti = donemlik_su_miktari * 2.16
                print("Donemlik toplam su tuketim ve atik su ucreti: ",
                      format(donemlik_atik_su_ucreti + donemlik_su_ucreti, ".2f"), "TL")
                print("Donemlik cTV tutari:", format(donemlik_su_miktari * 0.39, ".2f"), "TL")
                print("Donemlik kati atik toplama ucreti: ", 13, "TL")
                print("Donemlik kati atik bertaraf ucreti: ", 2.54, "TL")
                donemlik_toplam_fatura = donemlik_su_ucreti + donemlik_atik_su_ucreti + (
                        donemlik_su_miktari * 0.39) + 13 + 2.54 + \
                                         (donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100
                print("Donemlik toplam fatura tutari: ", format(donemlik_toplam_fatura, ".2f"), "TL")
                print("Donemlik devlete aktarilacak KDV tutari(%8): ",
                      format((donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100, ".2f"), "TL")
                print(
                    "Donemlik ilce belediyesine aktarilacak tutar: ", format(donemlik_su_miktari * 0.39 + 13, ".2f"),
                    "TL")
                print("Donemlik buyuksehir belediyesine aktarilacak tutar: ", 2.54, "TL")
                print("Donemlik iZSU payi: ", format(donemlik_toplam_fatura - (
                        ((donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100) + (
                            donemlik_su_miktari * 0.39 + 13) + 2.54),
                                                     ".2f"), "TL")
                self.devlet_payi += (donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100
                self.ilce_payi_toplam += donemlik_su_miktari * 0.39 + 13
                self.buyuksehir_payi += 2.54
                self.izsu_payi_toplam += donemlik_toplam_fatura - (
                        ((donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100) + (
                            donemlik_su_miktari * 0.39 + 13) + 2.54)
                if (donemlik_su_ucreti / sayac_gun_sayisi * 30 > self.su_tuketim_ucreti_max):
                    self.su_tuketim_ucreti_max = donemlik_su_ucreti / sayac_gun_sayisi * 30
                    self.su_tuketim_ucreti_max_abone_no = abone_no
                    self.abone_tipi_adi_max = "Resmi Daire"
                    self.su_tuketim_ucreti_max_miktari = donemlik_su_miktari / sayac_gun_sayisi * 30
                if (donemlik_su_ucreti / sayac_gun_sayisi * 30 > self.resmi_daire_su_tuketim_max):
                    self.resmi_daire_su_tuketim_max = donemlik_su_miktari / sayac_gun_sayisi * 30
                    self.abone_sayisi = abone_no
            elif (abone_tipi_kodu == 4):
                self.organize_sanayi_abone_sayisi += 1
                while True:
                    onceki_sayac = float(input("onceki sayac degerini giriniz: "))
                    if (onceki_sayac < 0):
                        print("Hatali veri girisi!")
                        continue
                    simdiki_sayac = float(input("simdiki sayac degerini giriniz: "))
                    while (simdiki_sayac < onceki_sayac):
                        print("Hatali veri girisi!")
                        simdiki_sayac = float(input("simdiki sayac degerini giriniz: "))
                    sayac_gun_sayisi = int(
                        input("onceki ve simdiki sayac okuma tarihleri arasindaki gun sayisini giriniz: "))
                    while (sayac_gun_sayisi <= 0):
                        print("Hatali veri girisi!")
                        sayac_gun_sayisi = int(
                            input("onceki ve simdiki sayac okuma tarihleri arasindaki gun sayisini giriniz: "))
                    else:
                        break
                print("Abone no: ", abone_no)
                print("Abone tipi adi: Organize Sanayi")
                donemlik_su_miktari = simdiki_sayac - onceki_sayac
                self.organize_sanayi_su_tuketim = donemlik_su_miktari / sayac_gun_sayisi * 30
                print("Donemlik su tuketim miktari: ", format(donemlik_su_miktari, ".2f"), "ton")
                self.su_tuketim_miktari_toplam += donemlik_su_miktari / sayac_gun_sayisi * 30
                donemlik_su_ucreti = donemlik_su_miktari * 5
                if (
                        donemlik_su_miktari / sayac_gun_sayisi * 30 > 100 or donemlik_su_ucreti / sayac_gun_sayisi * 30 > 500):
                    self.aylik_100ton_veya_500tl += 1
                print("Donemlik su tuketim ucreti: ", format(donemlik_su_ucreti, ".2f"), "TL")
                self.organize_sanayi_su_ucreti += donemlik_su_ucreti / sayac_gun_sayisi * 30
                donemlik_atik_su_ucreti = donemlik_su_miktari * 2.5
                print("Donemlik toplam su tuketim ve atik su ucreti: ",
                      format(donemlik_atik_su_ucreti + donemlik_su_ucreti, ".2f"), "TL")
                print("Donemlik cTV tutari:", format(donemlik_su_miktari * 0.39, ".2f"), "TL")
                print("Donemlik kati atik toplama ucreti: ", 13, "TL")
                print("Donemlik kati atik bertaraf ucreti: ", 2.54, "TL")
                donemlik_toplam_fatura = donemlik_su_ucreti + donemlik_atik_su_ucreti + (
                        donemlik_su_miktari * 0.39) + 13 + 2.54 + \
                                         (donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100
                print("Donemlik toplam fatura tutari: ", format(donemlik_toplam_fatura, ".2f"), "TL")
                print("Donemlik devlete aktarilacak KDV tutari(%8): ",
                      format((donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100, ".2f"), "TL")
                print(
                    "Donemlik ilce belediyesine aktarilacak tutar: ", format(donemlik_su_miktari * 0.39 + 13, ".2f"),
                    "TL")
                print("Donemlik buyuksehir belediyesine aktarilacak tutar: ", 2.54, "TL")
                print("Donemlik iZSU payi: ", format(donemlik_toplam_fatura -
                                                     (((donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100) + (
                                                             donemlik_su_miktari * 0.39 + 13) + 2.54), ".2f"), "TL")
                self.devlet_payi += (donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100
                self.ilce_payi_toplam += donemlik_su_miktari * 0.39 + 13
                self.buyuksehir_payi += 2.54
                self.izsu_payi_toplam += donemlik_toplam_fatura - (
                        ((donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100) + (
                            donemlik_su_miktari * 0.39 + 13) + 2.54)
                if (donemlik_su_ucreti / sayac_gun_sayisi * 30 > self.su_tuketim_ucreti_max):
                    self.su_tuketim_ucreti_max = donemlik_su_ucreti / sayac_gun_sayisi * 30
                    self.su_tuketim_ucreti_max_abone_no = abone_no
                    self.abone_tipi_adi_max = "Organize Sanayi"
                    self.su_tuketim_ucreti_max_miktari = donemlik_su_miktari / sayac_gun_sayisi * 30
            elif (abone_tipi_kodu == 5):
                self.tarim_hayvan_sulama_abone_sayisi += 1
                while True:
                    onceki_sayac = float(input("onceki sayac degerini giriniz: "))
                    if (onceki_sayac < 0):
                        print("Hatali veri girisi!")
                        continue
                    simdiki_sayac = float(input("simdiki sayac degerini giriniz: "))
                    while (simdiki_sayac < onceki_sayac):
                        print("Hatali veri girisi!")
                        simdiki_sayac = float(input("simdiki sayac degerini giriniz: "))
                    sayac_gun_sayisi = int(
                        input("onceki ve simdiki sayac okuma tarihleri arasindaki gun sayisini giriniz: "))
                    while (sayac_gun_sayisi <= 0):
                        print("Hatali veri girisi!")
                        sayac_gun_sayisi = int(
                            input("onceki ve simdiki sayac okuma tarihleri arasindaki gun sayisini giriniz: "))
                    else:
                        break
                oran_kademe1 = sayac_gun_sayisi * 13 / 30
                oran_kademe2 = sayac_gun_sayisi * 20 / 30
                print("Abone no: ", abone_no)
                print("Abone tipi adi: ilce Tarimsal ve Hayvan Sulama")
                donemlik_su_miktari = simdiki_sayac - onceki_sayac
                self.tarim_hayvan_su_tuketim = donemlik_su_miktari / sayac_gun_sayisi * 30
                self.su_tuketim_miktari_toplam += donemlik_su_miktari / sayac_gun_sayisi * 30
                if (donemlik_su_miktari / sayac_gun_sayisi * 30 > 50):
                    self.tarimsal_50den_fazla += 1
                print("Donemlik su tuketim miktari: ", format(donemlik_su_miktari, ".2f"), "ton")
                if (donemlik_su_miktari <= oran_kademe1):
                    donemlik_su_ucreti = (donemlik_su_miktari * 1.45)
                    self.tarim_hayvan_su_ucreti += donemlik_su_ucreti / sayac_gun_sayisi * 30
                elif (donemlik_su_miktari <= oran_kademe2):
                    donemlik_su_ucreti = (oran_kademe1 * 1.45 + (donemlik_su_miktari - oran_kademe1) * 2.86)
                    self.tarim_hayvan_su_ucreti += donemlik_su_ucreti / sayac_gun_sayisi * 30
                else:
                    donemlik_su_ucreti = (oran_kademe1 * 1.45 + (oran_kademe2 - oran_kademe1) * 2.89 + (
                            donemlik_su_miktari - oran_kademe2 * 6.43))
                    self.tarim_hayvan_su_ucreti += donemlik_su_ucreti / sayac_gun_sayisi * 30
                print("Donemlik su tuketim ucreti: ", format(donemlik_su_ucreti), ".2f", "TL")
                if (donemlik_su_miktari <= oran_kademe1):
                    donemlik_atik_su_ucreti = (donemlik_su_miktari * 0.72)
                elif (donemlik_su_miktari <= oran_kademe2):
                    donemlik_atik_su_ucreti = (oran_kademe1 * 0.72 + (donemlik_su_miktari - oran_kademe1) * 1.44)
                else:
                    donemlik_atik_su_ucreti = (oran_kademe1 * 0.72 + (oran_kademe2 - oran_kademe1) * 1.44 + (
                            donemlik_su_miktari - oran_kademe2) * 3.22)
                if (
                        donemlik_su_miktari / sayac_gun_sayisi * 30 > 100 or donemlik_su_ucreti / sayac_gun_sayisi * 30 > 500):
                    self.aylik_100ton_veya_500tl += 1
                print("Donemlik atik su tuketim ucreti: ", format(donemlik_atik_su_ucreti, ".2f"), "TL")
                print("Donemlik toplam su tuketim ve atik su ucreti :",
                      format(donemlik_su_ucreti + donemlik_atik_su_ucreti, ".2f"), "TL")
                print("Donemlik cTV tutari: ", format(donemlik_su_miktari * 0.39, ".2f"), "TL")
                print("Donemlik kati atik toplama ucreti: ", 13, "TL")
                print("Donemlik kati atik bertaraf ucreti: ", 2.54, "TL")
                donemlik_toplam_fatura = donemlik_su_ucreti + donemlik_atik_su_ucreti + (
                        donemlik_su_miktari * 0.39) + 13 + 2.54 + \
                                         (donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100
                print("Donemlik toplam fatura :", format(donemlik_toplam_fatura, ".2f"), "TL")
                print("Donemlik devlete aktarilacak KDV tutari(%8): ",
                      format((donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100, ".2f"), "TL")
                print(
                    "Donemlik ilce belediyesine aktarilacak tutar: ", format(donemlik_su_miktari * 0.39 + 13, ".2f"),
                    "TL")
                print("Donemlik buyuksehir belediyesine aktarilacak tutar: ", 2.54, "TL")
                print("Donemlik iZSU payi: ", format(donemlik_toplam_fatura - (
                        ((donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100) + (
                            donemlik_su_miktari * 0.39 + 13) + 2.54),
                                                     ".2f"), "TL")
                self.devlet_payi += (donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100
                self.ilce_payi_toplam += donemlik_su_miktari * 0.39 + 13
                self.buyuksehir_payi += 2.54
                self.izsu_payi_toplam += donemlik_toplam_fatura - (
                        ((donemlik_su_ucreti + donemlik_atik_su_ucreti) * 8 / 100) + (
                            donemlik_su_miktari * 0.39 + 13) + 2.54)
                if (donemlik_su_ucreti / sayac_gun_sayisi * 30 > self.su_tuketim_ucreti_max):
                    self.su_tuketim_ucreti_max = donemlik_su_ucreti / sayac_gun_sayisi * 30
                    self.su_tuketim_ucreti_max_abone_no = abone_no
                    self.su_tuketim_ucreti_max_miktari = donemlik_su_miktari / sayac_gun_sayisi * 30
                    self.abone_tipi_adi_max = "Tarimsal ve Hayvan Sulama"
            while (True):
                abone_varmi = input("Baska abone var mi?(e/E/h/H karakterleri)")
                abone_list = ["e", "E", "h", "H"]
                if (abone_varmi not in abone_list):
                    print("Hatali deger girdiniz")
                else:
                    break
        su_ucreti_toplam = self.konut_hane_su_ucreti + self.isyeri_su_ucreti + self.resmi_daire_su_ucreti + self.organize_sanayi_su_ucreti + self.tarim_hayvan_su_ucreti

    def display_result(self):
        su_ucreti_toplam = self.konut_hane_su_ucreti + self.isyeri_su_ucreti + self.resmi_daire_su_ucreti + self.organize_sanayi_su_ucreti + self.tarim_hayvan_su_ucreti
        print("Konut tipi abone(hane)sayisi: ", format(self.konut_hane_sayisi_toplam), ", yuzdesi: %",
              format(self.konut_hane_sayisi_toplam / self.abone_sayisi * 100, ".2f"),
              ", aylik ortalama su tuketim miktari: ",
              format(self.konut_hane_su_tuketim_miktari / self.konut_hane_sayisi_toplam, ".2f"), "ton")
        print("isyeri tipi abone sayisi: ", self.isyeri_abone_sayisi, " yuzdesi: %",
              format(self.isyeri_abone_sayisi / self.abone_sayisi * 100, ".2f"),
              ", aylik ortalama su tuketim miktari: ", format(self.isyeri_su_tuketim / self.isyeri_abone_sayisi, ".2f"),
              "ton")
        print("Resmi daire abone sayisi:", self.resmi_daire_abone_sayisi, ", yuzdesi: %",
              format(self.resmi_daire_abone_sayisi / self.abone_sayisi * 100, ".2f"),
              ", aylik ortalama su tuketim miktari: ", format(self.isyeri_su_tuketim / self.isyeri_abone_sayisi, ".2f"),
              "ton")
        print("Organize sanayi abone sayisi:", self.organize_sanayi_abone_sayisi, ", yuzdesi: %",
              format(self.organize_sanayi_abone_sayisi / self.abone_sayisi * 100, ".2f"),
              ", aylik ortalama su tuketim miktari: ",
              format(self.organize_sanayi_su_tuketim / self.organize_sanayi_abone_sayisi, ".2f"), "ton")
        print("Tarimsal ve hayvan sulama abone sayisi:", self.tarim_hayvan_sulama_abone_sayisi, ", yuzdesi: %",
              format(self.tarim_hayvan_sulama_abone_sayisi / self.abone_sayisi * 100, ".2f"),
              ", aylik ortalama su tuketim miktari: ",
              format(self.tarim_hayvan_su_tuketim / self.tarim_hayvan_sulama_abone_sayisi, ".2f"), "ton")
        print("1.Kademe konut tipi abonelerin(hane)sayilari: ", self.konut_hane_sayisi_kademe1_toplam,
              ", konut tipi aboneleri icindeki yuzdesi: %",
              format(self.konut_hane_sayisi_kademe1_toplam / self.konut_hane_sayisi_toplam, ".2f"),
              ", aylik ortalama su tuketim miktari: ",
              format(self.konut_hane_su_tuketim_miktari_kademe1 / self.konut_hane_sayisi_kademe1_toplam, ".2f"), "ton")
        print("2.Kademe konut tipi abonelerin(hane)sayilari: ", self.konut_hane_sayisi_kademe2_toplam,
              ", konut tipi aboneleri icindeki yuzdesi: %",
              format(self.konut_hane_sayisi_kademe2_toplam / self.konut_hane_sayisi_toplam, ".2f"),
              ", aylik ortalama su tuketim miktari: ",
              format(self.konut_hane_su_tuketim_miktari_kademe2 / self.konut_hane_sayisi_kademe2_toplam, ".2f"), "ton")
        print("3.Kademe konut tipi abonelerin(hane)sayilari: ", self.konut_hane_sayisi_kademe3_toplam,
              ", konut tipi aboneleri icindeki yuzdesi: %",
              format(self.konut_hane_sayisi_kademe3_toplam / self.konut_hane_sayisi_toplam, ".2f"),
              ", aylik ortalama su tuketim miktari: ",
              format(self.konut_hane_su_tuketim_miktari_kademe3 / self.konut_hane_sayisi_kademe3_toplam, ".2f"), "ton")
        print("Aylik su tuketim miktari 50 tondan fazla olan ilce tarimsal ve hayvan sulama tipi abonelerin sayisi: ",
              self.tarimsal_50den_fazla,
              ", ve ilce tarimsal ve hayvan sulama tipi aboneler icindeki yuzdesi: %",
              format(self.tarimsal_50den_fazla / self.tarim_hayvan_sulama_abone_sayisi * 100, ".2f"))
        print(
            "Aylik su tuketim miktari 100 tondan yuksek veya aylik su tuketim ucreti 500 TLíden yuksek olan abonelerin (hanelerin) sayisi: ",
            self.aylik_100ton_veya_500tl)
        print(
            "sehit, gazi veya devlet sporcusu olan konut tipi abonelerin(hanelerin) sayisi: ",
            self.indirimli_hane_sayisi)
        print("Engelli olan konut tipi abonelerin(hanelerin) sayisi: ", self.engelli_hane_sayisi,
              ", ve konut tipi aboneler(haneler) icindeki yuzdeleri: %",
              format(self.engelli_hane_sayisi / self.konut_hane_sayisi_toplam * 100, ".2f"))
        print(", ve konut tipi aboneler(haneler) icindeki yuzdeleri: %",
              format(self.indirimli_hane_sayisi / self.konut_hane_sayisi_toplam * 100, ".2f"))
        print("Aylik su tuketim miktari en yuksek olan resmi daire tipi abonenin abone noísu: ",
              self.resmi_daire_abone_no_max, " ve aylik su tuketim miktari: ",
              format(self.resmi_daire_su_tuketim_max, ".2f"), "ton")
        print("Aylik su tuketim ucreti en yuksek olan konut tipi disindaki abonenin abone noísu: ",
              self.su_tuketim_ucreti_max_abone_no,
              " abone tipi adi: ", self.abone_tipi_adi_max, " aylik su tuketim miktari: ",
              format(self.su_tuketim_ucreti_max_miktari, ".2f"), "ton",
              " ve odedigi aylik su tuketim ucreti: ", format(self.su_tuketim_ucreti_max, ".2f"))
        print(
            "Konut tipi abonelerin aylik toplam su tuketim miktari: ",
            format(self.konut_hane_su_tuketim_miktari, ".2f"),
            "ton",
            " Bornova'nin aylik toplam su tuketim miktari icindeki yuzdesi: %",
            format(self.konut_hane_su_tuketim_miktari / self.su_tuketim_miktari_toplam * 100, ".2f"))
        print("isyeri tipi abonelerin aylik toplam su tuketim miktari: ", format(self.isyeri_su_tuketim, ".2f"), "ton",
              " Bornova'nin aylik toplam su tuketim miktari icindeki yuzdesi: %",
              format(self.isyeri_su_tuketim / self.su_tuketim_miktari_toplam * 100, ".2f"))
        print(
            "Resmi daire tipi abonelerin aylik toplam su tuketim miktari: ", format(self.resmi_daire_su_tuketim, ".2f"),
            "ton",
            " Bornova'nin aylik toplam su tuketim miktari icindeki yuzdesi: %",
            format(self.resmi_daire_su_tuketim / self.su_tuketim_miktari_toplam * 100, ".2f"))
        print("Organize sanayi tipi abonelerin aylik toplam su tuketim miktari: ",
              format(self.organize_sanayi_su_tuketim, ".2f"), "ton",
              " Bornova'nin aylik toplam su tuketim miktari icindeki yuzdesi: %",
              format(self.organize_sanayi_su_tuketim / self.su_tuketim_miktari_toplam * 100, ".2f"))
        print("Tarimsal ve hayvan sulama tipi abonelerin aylik toplam su tuketim miktari: ",
              format(self.tarim_hayvan_su_tuketim, ".2f"), "ton",
              " Bornova'nin aylik toplam su tuketim miktari icindeki yuzdesi: %",
              format(self.tarim_hayvan_su_tuketim / self.su_tuketim_miktari_toplam * 100, ".2f"))
        print("Bornova'nin aylik su tuketim miktari: ", format(self.su_tuketim_miktari_toplam, ".2f"), "ton")
        print("Konut tipi abonelerden(haneler) elde edilen toplam su tuketim ucreti: ",
              format(self.konut_hane_su_ucreti, ".2f"))
        print("isyeri tipi abonelerden elde edilen toplam su tuketim ucreti: ", format(self.isyeri_su_ucreti, ".2f"))
        print("Resmi daire tipi abonelerden elde edilen toplam su tuketim ucreti: ",
              format(self.resmi_daire_su_ucreti, ".2f"))
        print("Organize sanayi tipi abonelerden elde edilen toplam su tuketim ucreti: ",
              format(self.organize_sanayi_su_ucreti, ".2f"))
        print("Tarimsal ve hayvan sulama tipi abonelerden elde edilen toplam su tuketim ucreti: ",
              format(self.tarim_hayvan_su_ucreti, ".2f"))
        print("Tum abonelerden elde edilen aylik toplam tu tuketim ucreti: ", format(su_ucreti_toplam, ".2f"))
        print("ilgili donemde su faturalarindan  iZSU'nun elde ettigi gelir : ", format(self.izsu_payi_toplam, ".2f"))
        print("ilgili donemde su faturalarindan  ilce Belediyesi'nin elde ettigi gelir : ",
              format(self.ilce_payi_toplam, ".2f"))
        print("ilgili donemde su faturalarindan  Buyuksehir Belediyesi'nin elde ettigi gelir : ",
              format(self.buyuksehir_payi, ".2f"))
        print("ilgili donemde su faturalarindan  Devlet'in elde ettigi gelir : ", format(self.devlet_payi, ".2f"))
