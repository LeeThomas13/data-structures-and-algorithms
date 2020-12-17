# Yo Yo Yo! Welcome Back!

## Thats right, its another installment of the best coding blog on the net.

#### Todays Lesson: How to quicksort

## Steps:
1. We need a list to sort, and we need some logic
2. We start by making three functions, one to separate the list, another to pick a pivot point, and lastly one to compare the pointers to the pivot.
3. Whats a pivot you ask? Well its a point we randomly choose in the list that acts as a comparison. Well whats the point of that? Ill tell you, we set up two pointers, a left and a right, and compare their values to the pivot.
4. Now heres a breakdown, First we cut the list in half, and pick the left chunk. We then choose a pivot, ideally somewhere in the middle of the list. Then we set our left pointer to index 0 of the list, and our right pointer to the last index of the list.
5. We then start comparing the left pointer to the pivot, if the value at its current index is less the pivot, we increment the left pointers index up one. If the left pointers value at the current index is greater than or equal to the pivot, we pause the left and start incrementing the right pointer backwards through the list. We do this until we find a value that is less than the pointer.
6. Once we have our pointers aiming at two out of place values, we swap their values at their indices. So the left pointers value becomes the rights value and vice versa.
7. Once that is done, we repeat the process until the left and right pointer are aiming at the same index.
8. We then split the list we were working on in half and repeat.
9. Eventually we will end up with a beautifully sorted list thanks to the quick sort algorithm.

## I can hear you now, "Wow! Now I know quick sort! Thanks!"
### And my response to you is here is my PayPal ->
<br>

### paypal.com/thisisfake
