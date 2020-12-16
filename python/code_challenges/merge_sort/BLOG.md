# Oh hey there reader!

### Ready for another installment of the spectacular BLOG??!!

### Todays Topic: Merge Sort1!!1!

#### Breakdown:

1. We need an array to sort out.
2. We will then make a function that takes in that array and splits it in half!
3. this function will first check if the array is empty, or if its only one int long.
4. We then make three variables, the first will represent the mid point of the array (mid = len(arr)//2). the second will represent the first half of the array and the third will represent the latter half.
5. We then call our brand new function on the second and third variables to chop them in half again! This creates a recursive way to chop the array in half as many times as we need it to be.
6. Once we have chopped the original array into pieces, we will make another function to merge them back together, in order.
7. We will call this function merge, and we will pass in the second and third arrays we made on line #4. Lets call them a and b. We will also make another array called c.
8. We then use a while loop: While a and b have values we will do this. If a is greater than b, we we add b to the end of c and remove b, else we add a to the end of c and remove a.
9. Now that either a or b is empty, we make two more while loops. If A still has a value add a to the end of c, and remove a. If B still has a value add b to the end of c and remove b.
10. Finally we return c.
11. And there you have it! A functioning merge sort algortithm that can handle any size array that you need sorted!. Granted this approach is a big cost prohibitive, with a Big O of O(nlogn).

