require_relative "./graph.rb"

graph = Graph.new
raise "Error in Size" unless graph.Size() == 0
raise "Error in IsEmpty" unless graph.IsEmpty()

puts "All tests are OK"
