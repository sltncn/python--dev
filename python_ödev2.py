#SORU 1


# In order to use alphabets and digits I import string library.
import string

# I take inputs from user to use in decryption function.
initial_text = str(input("Please enter the encrypted text: "))
shift_number = int(input("Please enter the shift number: "))

# I create a function with two parameters: encrypted text and shift number.
def decryption(text , shift):
   
   # with string library functions I make lists of lower case letters , upper case letters and digits.
   # I make list because i want to find and convert each letter and digit.
    alphabet_lower = list(string.ascii_lowercase)
    alphabet_upper = list(string.ascii_uppercase)
    digits = list(string.digits)
    
    # I make empty output list which is new decyrpted text.
    new_text = []
    
    # I make a loop that runs while checking every character in input text and ends after that.
    for ch in text:
    
        # If character is space it remains same and function adds it to new text list.
        if ch == ' ':
            new_text.append(' ')
        
        # If it is lower case letter function finds its order, adds shift number, 
        # mods with 26 in order to reduct it to alphabet range after that it finds back
        #  its place in alphabet and adds to the text list.
        elif ch in alphabet_lower :
            position = alphabet_lower.index(ch)
            new_position = (position + shift) % 26
            new_letter = alphabet_lower[new_position]
            new_text.append(new_letter)
        
        #Does same thing with lower case one .   
        elif ch in alphabet_upper :
            position = alphabet_upper.index(ch)
            new_position = (position + shift) % 26
            new_letter = alphabet_upper[new_position]
            new_text.append(new_letter)
        
        # Also does same but this time I mod with 10 because there are 10 characters in digits list.
        elif ch in digits :
            position = digits.index(ch)
            new_position = (position + shift) % 10
            new_text.append(digits[new_position])

    #Now I have a list full of new characters so I add them one after.
    new_text = ''.join(new_text)
    
    #Getting feedback
    return new_text

print(decryption(initial_text , shift_number))       
       




#SORU 2


# A function that takes row as a parameter. Row is the desired row value in the sample.
def draw(row):

    # row number is divided by two because i will print same line two times, eventually row number remains same.
  n = int(row/2)

  # for each number from 0 to n; it prints n-i-1 times space, 2*i+2 times * and creates new line; this process repeats 2 times for each i value in n.
  for i in range(n):  
      for a in range(2):
          for j in range(n-i-1): 
              print(" ", end = "  ")
          
          for j in range(2*i+2):
              print("*", end="  ")
          print()
    
draw(10)







#SORU 3



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



          
