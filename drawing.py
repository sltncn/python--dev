



#First we should import "NumPy" library as "np" and import matplotlib.pyplot as plt in order to work with statetical functions and plotting functions.

#In the next line a random computer file is assigned as variable, we should use open() and read() functions to open file.
# And we should make it list in order to use array functions ; örnekler = list(herhangi_bir_bilgisayar_dosyası)
örnekler = herhangi_bir_bilgisayar_dosyası

# X is a array that holds the data that exist in the first column of örnekler list, Y is a array that holds the data in the second column of it.
X = örnekler[:,0]
Y = örnekler[:,1]

#Here mean_x,y variables holds average values of X and Y array elements.
mean_x = np.mean(X)
mean_y = np.mean(Y)

# m variable holds lenght of X array.
m = len(X)

#Numerator and denominator are defined and initialized by 0.
numerator = 0
denominator = 0

#A loop that runs for each value in 0 to m.
for i in range(m) :
  
   #numerator is equal to previous numerator value + (i'th element in X array - average of X) times (i'th element in Y array - average Y)
    numerator += (X[i] - mean_x) * (Y[i] - mean_y)
    # denominator is equal to previous denominator value + ( i'th element in X array - average X) squared
    denominator += (X[i] - mean_x) ** 2


# final numerator value that comes out from loop is divided by final denominator value and it is assigned to m float variable.
# c is a float variable that holds (average value of Y array elements) - ( m times average value of Y array element)
m = numerator / denominator
c = mean_y - (m * mean_y)

# that line prints m value instead of {m} and c value instead of {c} in "m = {m} c = {c}"
print(f'm = {m} c = {c}')

# first line takes maximum value in elements of X array and assign it to max_x ; second line takes minimum value in elements of Y array and assign it to min_x.
max_x = np.max(X)
min_x = np.min(Y)

# np.linspace (min_x, max_x) function returns array that consist 50 elements which are equally spaced numbers between minimum Y value and maximum X value.
x = np.linspace (min_x, max_x)
y = c + m * x # multiply x array elements by m and add them c. It is assigned as y array which consists these new elements.

# takes x values from "x" array, y values from "y" array, makes green graph line with these (x,y) pairs and line's name is 'Çizgi'.
plt.plot(x, y, 'g', label = 'Çizgi')
# takes x values from "X" array, y values from "Y" array, makes red dashed graph line with these (X,Y) pairs and line's name is 'Veriler'.
plt.plot(X, Y, 'rh', label = 'Veriler')

# x axis is named as 'İlk sütundaki veri', y axis is named as 'İkinci sütundaki veri'.
#  legend() function draws these two lines in same graph and show() prints the graph.
plt.xlabel('İlk sütundaki veri')
plt.ylabel('İkinci sütundaki veri')
plt.legend()
plt.show()



          
