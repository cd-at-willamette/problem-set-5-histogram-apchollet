from pgl import *


#1a
def create_histogram_array(data:list[int])->list[int]:
    histogram = [data.count(digit) for digit in range(10)]
    return histogram



#1b
def print_histogram(hist:list[int]) -> None:

    new_list = []
    for i in range(10):
        new_list.append(str(i) + ": " + hist[i] * '*')
        print(new_list[i])

#1c
def graph_histogram(hist:list[int], width:int, height:int) -> None:

    def my_rect(x,y,w,h,color):
        rect = GRect(x,y,w,h)
        rect.set_filled(True)
        rect.set_color(color)
        gw.add(rect)



# Some testing printouts for your use!
PI_DIGITS = [3,1,4,1,5,9,2,6,5,3,5,5,8,9,7,9]
hist = create_histogram_array(PI_DIGITS)
print(hist)
print_histogram(hist) # uncomment to test
graph_histogram(hist, 400, 400) # uncomment to test

