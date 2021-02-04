import  numpy as np
import matplotlib.pyplot as plt
import math
#x = np.array([ j for j in range(-180,195, 15)],float)
#y = np.array([math.sin(math.radians(x[i])) for i in range(len(x))],float)
x = [0.88,1.68,2.30,2.80,3.50,4.11,4.78,5.00,6.50,7.20,8.90,9.30,9.33,9.89,10.2]
y = [0.59490, -0.10877, -0.61806, -0.80887, -0.80546, -0.53678, 0.06751, 0.27987, 0.82859, 0.57152, -0.76138,-0.83725,-0.83904, -0.77941, -0.65506 ]

def Generate_List(start, stop, step):
    k = start
    ls = []
    while k < stop:
        ls.append(k)
        k+=step
    return ls

xplt = Generate_List(1,10,0.1)
form_all, global_grunge, local_grunge = [],[], []


def simp_Deriv(xp):
    return -(math.cos(math.cos(xp)) * math.sin(xp))
def simp_Sec_Deriv(xp):
    return -(math.sin(math.cos(xp)) * (math.sin(xp)**2) + math.cos(math.cos(xp))*math.cos(xp))
def deriv(x_plt,y_plt, h):
    print(len(x_plt))
    deriv_list = []
    for i in range(len(x_plt)):
        if i == 0:
            lev = (y_plt[i+1] - y_plt[i])/h
            deriv_list.append(lev)
        elif i > 0 and i < len(x_plt)-1:
            center = (y_plt[i+1] - y_plt[i-1]) /(2*h)
            deriv_list.append(center)
        elif i == len(x_plt)-1:
            prav = (y_plt[i]-y_plt[i-1])/h
            deriv_list.append(prav)
    return deriv_list
def sec_deriv(x_plt,y_plt, h):
    print(len(x_plt))
    deriv_list = []
    for i in range(len(x_plt)):
        if i == 0:
            lev = (y_plt[i+1] - y_plt[i])/h
            deriv_list.append(lev)
        elif i > 0 and i < len(x_plt)-1:
            center = (y_plt[i+1] + y_plt[i-1]-2*y_plt[i]) /(h**2)
            deriv_list.append(center)
        elif i == len(x_plt)-1:
            prav = (y_plt[i]-y_plt[i-1])/h
            deriv_list.append(prav)
    return deriv_list
def Search_OF_Gap(x_arr, xp_s):
    minm,mid,maxm = 0,0,0
    i = 0
    while i != len(x_arr) and xp_s > x_arr[i]:
        i +=1
    if i != 0:
        i-=1
    if i <= len(x_arr)-2 and i != 0:
        minm,mid,maxm = x_arr[i-1],x_arr[i],x_arr[i+1]
    elif i == len(x_arr):
        minm,mid,maxm = x_arr[i-3],x_arr[i-2],x_arr[i-1]
    elif i == len(x_arr) - 1:
        minm, mid, maxm = x_arr[i-2 ], x_arr[i-1], x_arr[i]
    elif i  == 0:
        minm, mid, maxm = x_arr[i], x_arr[i+1], x_arr[i + 2]
    res_list = [minm,mid,maxm]
    return res_list
def Formula(xp):
    yp = math.sin(math.cos(xp))
    return yp
def Kvadrat_Kusoch(x_array,y_array, xp):
    gap_list = Search_OF_Gap(x_array,xp)
    i = np.where( x_array == gap_list[1])[0]
    a = (y_array[i+1] - y_array[i-1])/((x_array[i+1] - x_array[i-1]) * (x_array[i+1] - x_array[i])) - (y_array[i] - y_array[i-1])/((x_array[i] - x_array[i-1]) * (x_array[i+1] - x_array[i]))
    b = (y_array[i] - y_array[i-1])/(x_array[i] - x_array[i-1]) - a*(x_array[i] + x_array[i-1])
    c = y_array[i-1] -b*x_array[i-1] - a*(pow(x_array[i-1], 2))

    yp = c + b*xp + a*(xp**2)
    return yp
def Global_LaGrange(x_arr, y_arr, xp):
    yp =0
    for i in range(len(x_arr)):
        p =1
        for j in range(len(x_arr)):
            if j != i:
             p*= ((xp - x_arr[j])/(x_arr[i]-x_arr[j]))
        yp += y_arr[i]*p
    return  yp
def Local_Grunge(x_arr, y_arr, xp):
    yp =0
    ind_arr = Search_OF_Gap(x_arr,xp)
    temp_arr = []
    for k in range(3):
        temp_arr.append(y_arr[x_arr.index(ind_arr[k])])
    for i in range(3):
        p =1
        for j in range(3):
            if j != i:
             p*= ((xp - ind_arr[j])/(ind_arr[i]-ind_arr[j]))
        yp += temp_arr[i]*p
    return  yp

der_list, sec_der_list =[], []
for xp in xplt:
    form_all.append(Formula(xp))
    global_grunge.append(Global_LaGrange(x,y,xp))
    local_grunge.append(Local_Grunge(x,y,xp))
    der_list.append(simp_Deriv(xp))
    sec_der_list.append(simp_Sec_Deriv(xp))
t_der = deriv(xplt,global_grunge,0.1)
s_t_der = sec_deriv(xplt, global_grunge,0.1)
def print_data_one(xpl, ypl, glob, loc):
    print("x        y         L         kv")
    for i in range(len(xpl)):
        print(f"{xpl[i]}   {ypl[i]}    {glob[i]}   {loc[i]}")
def print_data_two(xpl, ypl, der_one):
    print("x        form         dy/dx")
    for i in range(len(xpl)):
        print(f"{xpl[i]}   {ypl[i]}    {der_one[i]} ")
def print_data_three(xpl, ypl, der_one):
    print("x        form         d2y/d2x")
    for i in range(len(xpl)):
        print(f"{xpl[i]}   {ypl[i]}    {der_one[i]} ")
print_data_one(xplt, form_all, global_grunge, local_grunge)
print_data_two(xplt, der_list, t_der)
print_data_three(xplt, sec_der_list, s_t_der)
plt.plot(x,y,'ro', xplt,form_all,'b-')
#plt.plot(xplt,der_list, 'r-')
plt.plot( xplt,global_grunge,'r-')
plt.plot( xplt,local_grunge,'g-')
#plt.plot(xplt, t_der,'b-')
plt.plot(xplt, s_t_der, "g-")
plt.show()

