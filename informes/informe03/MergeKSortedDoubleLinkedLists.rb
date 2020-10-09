require_relative "./DoubleLinkedList.rb"

# First, let's create the input of no decreasing ordered lists
list1 = DoubleLinkedList.new
list1.AddRight 1
list1.AddRight 4
list1.AddRight 5

list2 = DoubleLinkedList.new
list2.AddRight 1
list2.AddRight 3
list2.AddRight 4

list3 = DoubleLinkedList.new
list3.AddRight 2
list3.AddRight 6

puts "Input"
list1.Print
list2.Print
list3.Print

# INF is going to represent a number bigger than all our numbers
# lists is going to store our lists
# number_lists is going to represent k, the number of lists we want to merge
INF = 2 ** 63 - 1
lists = [list1, list2, list3]
number_lists = lists.length()

# result is going to store our final ordered double linked list
# number_elements is going to have the number of elements in the result
result = DoubleLinkedList.new
number_elements = 0

# list_size is going to store the length of each list
# current_pos is going to store the index in which we are at on each list
list_length = Array.new(number_lists)
current_pos = Array.new(number_lists)

# We are storing the length of each list to query them in O(1) instead of O(n)
for i in 0 ... number_lists do
 list_length[i] = lists[i].Size
 current_pos[i] = 0
 number_elements += list_length[i]
end

for i in 0 ... number_elements do
  # minimum is going to store two values, the minimum number we have until now
  # and the index of which list this minimum number is from
  minimum = [INF, -1]
  # For each list, if it's first element is less than our current minimum
  # we are going to store its value and from which list it was member of
  for j in 0 ... number_lists do
    if current_pos[j] < list_length[j] && lists[j].Head < minimum[0]
      minimum[0] = lists[j].Head
      minimum[1] = j
    end
  end
  # First, we add the minimum number of all the heads to our result
  result.AddRight minimum[0]
  # Then, we erase the head of that list
  lists[minimum[1]].RemoveLeft
  current_pos[minimum[1]] += 1
end

# Finally, we print our answer
puts "Output:"
result.Print
