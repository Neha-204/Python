# Create a list of colors from comma-separated color names entered by user. Display first and
# last colors.

n = int(input("Enter the no of colours: "))
color_list = []
for i in range(n):
 color = input("Enter the colour: ")
 color_list.append(color)
 print(color_list)
 print("The first color is:", color_list[0])
 print("The last color is:", color_list[-1])

