import webbrowser
import math

ans = math.pow(2,38)

print("Copy this value:",ans)

num = input("and paste it here: ")

url = "http://www.pythonchallenge.com/pc/def/"+num+".html"

webbrowser.open(url)
