import io
import os
items = os.listdir("..\items")

print(items)
x = 0
print("<table>")
for item in items:
    print("<td><button onclick='selectItem("+item+")'><img id= '"+item+"' src='../items/"+item+"'></button></td>")



print("</table>")
