require_relative "./dijkstra.rb"
require_relative "./graph.rb"
require_relative "./min_heap.rb"

def GetPath u, parent
  path = []
  while u != -1
    path.push(u)
    u = parent[u]
  end
  len = path.length
  for i in 0 .. len / 2 - 1
    path[i], path[len - 1 - i] = path[len - 1 - i], path[i]
  end
  return path
end

def PrintPath path
  len = path.length
  for i in 0 .. len - 1
    if i > 0
      print " -> "
    end
    print "#{path[i]}"
  end
  puts ""
end

def main
  puts "Report 5 - Dijkstra's algorithm"
  puts ""

  graph = Graph.new(5)
  graph.AddEdge(0, 1, 10)
  graph.AddEdge(0, 3, 5)
  graph.AddEdge(1, 3, 2)
  graph.AddEdge(1, 2, 1)
  graph.AddEdge(2, 4, 4)
  graph.AddEdge(3, 1, 3)
  graph.AddEdge(3, 2, 9)
  graph.AddEdge(3, 4, 2)
  graph.AddEdge(4, 0, 7)
  graph.AddEdge(4, 2, 6)

  distance, parent = Dijkstra(graph, 0)

  for i in 0 .. graph.Size - 1
    puts "Shortest path from 0 to #{i}: #{distance[i]}"
    print "Path: "
    PrintPath(GetPath(i, parent))
    puts ""
  end
end

main
