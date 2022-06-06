#import the required framework
from flask import Flask, request
app = Flask(__name__)
import math

#assigning URLs using the python decorator that Flask provides
@app.route('/median')
#define the logic to find the median number
def medianNumber():
    val = request.args.getlist('value')
    #converting string to integer before applying sort function
    num = []
    for i in val:
        num.append(int(i))
    #sort the elements
    num.sort()
    #find the length
    n = len(num)
    #find the index of the middle element
    m = n // 2
    #For odd set of elements, the median value is the middle one
    #For even set of elements, the median value is the mean of two middle elements
    if n % 2 == 0:
        z = (int(num[m - 1]) + int(num[m])) / 2
        return str(z)
    else:
        return str(num[m])


#assigning URLs using the python decorator that Flask provides
@app.route('/max')
#define the logic to find the max number
def maxNumber():
  val = request.args.getlist('value')
  #converting string to integer before applying sort function
  num = []
  for i in val:
      num.append(int(i))
  #sort the elements
  num.sort()
  #list slicing to find the max element
  return str(num[-1])


#assigning URLs using the python decorator that Flask provides
@app.route('/min')
#define the logic to find the minimum number
def minNumber():
  val = request.args.getlist('value')
  #converting string to integer before applying sort function
  num = []
  for i in val:
      num.append(int(i))
  #sort the elements
  num.sort()
  #list slicing to find the min element
  return str(num[0])


#assigning URLs using the python decorator that Flask provides
@app.route('/avg')
#define the logic to find the average number
def average():
  num = request.args.getlist('value')
  #find the length
  n = len(num)
  #avg = sum of the elements/ total number of elements
  s = 0
  for i in num:
      s = s + int(i)
  avg = s/n
  return str("{:.2f}".format(avg))


#assigning URLs using the python decorator that Flask provides
@app.route('/percentile/')
#define the logic to find the qth percentile
def percentile():
  val = request.args.getlist('value')
  q = request.args.get('q')
  #converting string to integer before applying sort function
  num = []
  for i in val:
      num.append(int(i))
  #sort the elements
  num.sort()
  #find the length of the list
  n = len(num)
  #find the index of a number
  pct = (int(q)/100)*n
  #if the index is decimal value then find the nearest index above the decimal value
  r = math.ceil(pct) - 1
  return str(num[r])


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
