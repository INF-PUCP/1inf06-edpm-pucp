require "set"
require_relative "./graph.rb"

def PrintNodes nodes
  print "Nodes:"
  nodes.each do |node|
    print " #{node}"
  end
  puts ""
end

def PrintEdges edges
  print "Edges:"
  edges.each do |edge|
    print " (#{edge.from}, #{edge.to})"
  end
  puts ""
end

graph = Graph.new
raise "Error in Size" unless graph.Size() == 0
raise "Error in IsEmpty" unless graph.IsEmpty()

graph.AddNode(0)
graph.AddNode(1)
graph.AddNode(2)
graph.AddNode(3)
graph.AddNode(4)
graph.AddNode(5)

raise "Error in Size" unless graph.Size() == 6

# 0 --> 1     2
# |   ^ ^   / |
# |  /  |  /  |
# v /   | v   v
# 3 <-- 4     5 <--
#             |   |
#             -----
graph.AddEdge(0, 1)
graph.AddEdge(0, 3)
graph.AddEdge(2, 4)
graph.AddEdge(2, 5)
graph.AddEdge(3, 1)
graph.AddEdge(4, 3)
graph.AddEdge(5, 5)

raise "Error in AddEdge" unless graph.IsConnected(0, 1)
raise "Error in AddEdge" unless graph.IsConnected(0, 3)
raise "Error in AddEdge" unless graph.IsConnected(2, 4)
raise "Error in AddEdge" unless graph.IsConnected(2, 5)
raise "Error in AddEdge" unless graph.IsConnected(3, 1)
raise "Error in AddEdge" unless graph.IsConnected(4, 3)
raise "Error in AddEdge" unless graph.IsConnected(5, 5)

raise "Error in AddEdge" unless not graph.IsConnected(0, 2)
raise "Error in AddEdge" unless not graph.IsConnected(1, 2)
raise "Error in AddEdge" unless not graph.IsConnected(3, 0)
raise "Error in AddEdge" unless not graph.IsConnected(5, 2)
raise "Error in AddEdge" unless not graph.IsConnected(4, 5)

PrintNodes(graph.GetNodeSet)
PrintEdges(graph.GetEdgeSet)


graph.RemoveNode(4)
# 0 --> 1     2
# |   ^       |
# |  /        |
# v /         v
# 3           5 <--
#             |   |
#             -----
PrintNodes(graph.GetNodeSet)
PrintEdges(graph.GetEdgeSet)

graph.RemoveEdge(5, 5)
# 0 --> 1     2
# |   ^       |
# |  /        |
# v /         v
# 3           5
PrintNodes(graph.GetNodeSet)
PrintEdges(graph.GetEdgeSet)

graph.Clear()
raise "Error in Clear" unless graph.IsEmpty

puts "All tests are OK"
