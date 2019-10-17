def knapsackDynamicProg(profit, bobot, kapasitas):
    
    # Fungsi ini akan mengembalikan item dengan profit yang maximum tetapi tidak melalui batas 
    #Profit[i] adalah profit ke item berapa dn bobot[i] menunjukan bobot dari item ke berapa
   
    #for 1 <= i <= n : perulangan untuk mengakses banyaknya item.

    # n = ukuran profit(berapa banyak item profit)
    n = len(profit) - 1
 
    # m[i][w] akan menyimpan maximum profit yang bisa diambil 

    m = [[-1]*(kapasitas + 1) for _ in range(n + 1)]
 
    return mencariMaxProfit(profit, bobot, m, n, kapasitas)
 
 
def mencariMaxProfit(profit, bobot, m, i, w): 
    # Mencari  maximum profit dimana bobot harus lebih kecil sama dengan kapsitas
    # w : kapasitas 
    if m[i][w] >= 0:
        return m[i][w]
 
    if i == 0:
        q = 0
    elif bobot[i] <= w: 
        q = max( mencariMaxProfit(profit, bobot,
                                m, i - 1 , w - bobot[i])
                + profit[i],
                mencariMaxProfit(profit, bobot,
                                m, i - 1 , w))
    else:
        q =  mencariMaxProfit(profit, bobot,
                            m, i - 1 , w)
    m[i][w] = q
    return q


n = int(input('Masukan banyaknya item: '))
profit = input('Masukan Profit sesuai dengan ke-{} item : '.format(n)).split()
profit = [int(p) for p in profit]
profit.insert(0, None) 

bobot= input('Masukan bobot sesuai dengan ke-{} item : '.format(n)).split()
    
bobot = [int(b) for b in bobot]
bobot.insert(0, None) 

kapasitas = int(input('Masukan bobot Maximum: '))

hasil = knapsackDynamicProg(profit, bobot, kapasitas)

print('Maximum profit yang dapat dibawa adalah :', hasil)

#print('Maximum profit yang dapat dibawa adalah :', hasil)


