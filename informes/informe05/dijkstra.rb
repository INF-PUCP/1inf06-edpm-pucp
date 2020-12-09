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
