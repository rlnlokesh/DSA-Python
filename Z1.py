# a = open("C:\\Users\\HP\\Videos\\text.txt","a")
# a.write("\nIam buddy")
#
# a.close()

# a = open("C:\\Users\\HP\\Videos\\text.txt","r")
# a_out = open("C:\\Users\\HP\\Videos\\text_out.txt","w")
# for line in a:
#     tokens = line.split(' ')
#     a_out.write("wordcount:" +str(len(tokens))+ line)
#     print(len(tokens))
#
# a.close()
# a_out.close()

# x = input("enter number 1 : ") #by default it is string
# y = input("enter number 2 : ")
# try:
#     z = int(x)/int(y)
# except Exception as e:
#     print("Error Raised ",e)
#     z = None
# print("Division is: ",z)
#
# class Accident(Exception):
#     def __init__(self,msg):
#         self.msg = msg
#
#     def print_exception(self):
#         print("user defined exception is ",self.msg)
#
# try:
#     raise Accident("Two Cars Crashed")
# except Accident as e:
#     e.print_exception()

#
# def remote_comtrol():
#     yield "cnn"
#     yield "Espn"
#
# itr = remote_comtrol()
# print(type(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))


def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

for f in fib():
    if f>13:
        break
    print(f)