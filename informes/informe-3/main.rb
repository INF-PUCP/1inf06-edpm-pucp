require_relative "./DoubleLinkedList.rb"

list1 = DoubleLinkedList.new
raise "Error in IsEmpty" unless list1.IsEmpty

list1.Print
list1.AddRight 2
list1.Print
list1.AddRight 3
list1.Print
raise "Error in AddRight" unless list1.Size == 2

raise "Error in Head" unless list1.Head == 2
list1.RemoveLeft
list1.Print
raise "Error in RemoveLeft" unless list1.Size == 1
raise "Error in Head" unless list1.Head == 3
list1.RemoveRight
list1.Print
raise "Error in RemoveRight" unless list1.IsEmpty

list1.AddLeft 1
list1.Print
list1.AddRight 2
list1.Print
list1.AddLeft 3
list1.Print
list1.AddRight 4
list1.Print
list1.Remove 3
list1.Print
raise "Error in Remove" unless list1.Size == 3

list1.Remove 2
list1.Print
raise "Error in Remove" unless list1.Size == 2

puts "All tests are OK"
