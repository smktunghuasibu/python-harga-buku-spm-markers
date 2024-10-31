def harga_bayaran(jenisbuku, kuantiti):
    if jenisbuku==1:
        harga_seunit=6.00
        kadardiskaun=10
    elif jenisbuku==2:
        harga_seunit=7.50
        kadardiskaun=8
    else: 
        harga_seunit=8.90
        kadardiskaun=5
    potongan_harga=kuantiti*harga_seunit*(kadardiskaun/100)
    harga_total=(kuantiti*harga_seunit)-potongan_harga
    return potongan_harga,harga_total

def main():
    print("Senarai belian buku:")
    print("1.Latihan Pasti A,Bahasa Melayu,Tingkatan 1")
    print("2.Latihan Pasti A,Bahasa Melayu,Tingkatan 2")
    print("3.Latihan Pasti A,Bahasa Melayu,Tingkatan 3")
    while True:
        jenisbuku = int(input("Masukkan jenis buku yang dibeli (1-3): "))
        if jenisbuku > 3 or jenisbuku < 1:
            print("Sila masukkan nombor 1 hingga 3 sahaja.")
        else:
            break # exit when no error 
    kuantiti=int(input("Masukkan kuantiti buku yang dibeli:"))
    potongan_harga,harga_total = harga_bayaran(jenisbuku,kuantiti)
    print("Potongan harga yang diperoleh ialah RM", round(potongan_harga,2))
    print("Jumlah harga yang perlu dibayar ialah RM", round(harga_total,2))
    
if __name__ == "__main__":
    main()
