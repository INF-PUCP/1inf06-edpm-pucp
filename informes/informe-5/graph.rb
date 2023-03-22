require "set"

class Edge
  attr_accessor :to, :weight

  def initialize to, weight
    self.to = to
    self.weight = weight
  end
end

class Graph
  attr_accessor :adj, :nodes

  def initialize n
    self.adj = Hash.new
    self.nodes = n
    for u in 0 .. n - 1
      self.adj[u] = Set.new
    end
  end

  def AddEdge from, to, weight
    self.adj[from] << Edge.new(to, weight)
  end

  def Size
    return self.nodes
  end

  def GetNeighbors from
    return self.adj[from]
  end
end
