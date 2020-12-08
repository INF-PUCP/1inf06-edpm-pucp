require_relative "./graph.rb"
require_relative "./min_heap.rb"

INF = 1e18

def Dijkstra graph, origin
  distance = Array.new(graph.Size)
  parent = Array.new(graph.Size)

  for v in 0 .. graph.Size - 1
    distance[v] = INF
    parent[v] = -1
  end
  distance[origin] = 0

  q = MinHeap.new
  q.Push(Path.new(0, origin))

  while not q.IsEmpty? do
    path = q.GetMin()
    q.Pop() 
    u = path.node
    if path.weight != distance[u]
      next
    end

    neighbors = graph.GetNeighbors(u)
    neighbors.each do |edge|
      v = edge.to
      w = edge.weight
      if distance[u] + w < distance[v]
        distance[v] = distance[u] + w
        parent[v] = u
        q.Push(Path.new(distance[v], v))
      end
    end
  end

  return distance, parent
end

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
