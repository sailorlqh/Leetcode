def quicksort(left, right):
	pivot = array[left]
	pivot_index = left
	i = left
	j = right
	if(left == right):
		return
	while(left < right):
		while(array[right] > pivot and right > left):
			right -= 1
		if(right > left):
			array[left] = array[right]
			array[right] = pivot
			pivot_index = right
		else:
			break
		while(array[left] < pivot and left < right):
			left += 1
		if(left < right):
			array[right] = array[left]
			array[left] = pivot
			pivot_index = left
		else:
			break
	quicksort(i, pivot_index)
	quicksort(pivot_index + 1, j)

array = [9, 4,2,1,3,8,5,7,6,10]
quicksort(0, len(array) -1)
print(array)