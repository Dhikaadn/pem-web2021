saldoAwal = int(input("masukan saldo awal: "))
sisaSaldo = saldoAwal
pengeluaran = 0
while(pengeluaran!= -1):
    pengeluaran = int(input("masukan pengeluaran: "))
    if(pengeluaran>0)and((sisaSaldo-pengeluaran)>0):
        sisaSaldo = sisaSaldo-pengeluaran
    else:
        if(pengeluaran!= -1):
            print("sisa saldo anda tidak cukup",end="")
        break
print("sisa saldo",sisaSaldo)
        
