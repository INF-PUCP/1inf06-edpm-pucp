class Node
  attr_accessor :value, :neighbors

  def initialize value
    self.value = value
    self.neighbors = Hash.new
  end
end

class Edge
  attr_accessor :from, :to

  def initialize from, to
    self.from = from
    self.to = to
  end
end

class Graph
  attr_accessor :nodes

  def initialize
    self.nodes = Hash.new
  end

  def Size
    return self.nodes.size()
  end

  def IsEmpty
    return self.nodes.empty?()
  end

  def Clear
    self.nodes.clear()
  end

  def AddNode id
    new_node = Node.new(id)
    self.nodes[id] = new_node
  end

  def RemoveNode id
    raise "Node doesn't exist" unless self.NodeExists(id)

    self.nodes.delete(id);
    self.nodes.each do |node_id, node_ptr|
      if node_ptr.neighbors.key?(id)
        node_ptr.neighbors.delete(id)
      end
    end
  end

  def GetNode id
    return self.nodes[id]
  end

  def NodeExists id
    return self.nodes.key?(id);
  end

  def AddEdge from, to
    if not self.NodeExists(from)
      self.AddNode(from)
    end

    if not self.NodeExists(to)
      self.AddNode(to)
    end

    self.nodes[from].neighbors[to] = nodes[to]
  end

  def RemoveEdge from, to
    raise "Nodes don't exist" unless self.NodeExists(from) and self.NodeExists(to)
    raise "Edge doesn't exist" unless self.nodes[from].neighbors.key?(to)

    self.nodes[from].neighbors.delete(to)
  end

  def IsConnected from, to
    if not self.NodeExists(from) or not self.NodeExists(to)
      return false
    end

    return self.nodes[from].neighbors.key?(to)
  end

  def GetNodeSet
    node_set = Set.new

    self.nodes.each do |node_id, node_ptr|
      node_set.add(node_id)
    end

    return node_set
  end

  def GetEdgeSet
    edge_set = Set.new

    self.nodes.each do |from_id, from_ptr|
      from_ptr.neighbors.each do |to_id, to_ptr|
        new_edge = Edge.new(from_id, to_id)
        edge_set.add(new_edge)
      end
    end

    return edge_set
  end

  def GetNeighbors id
    raise "Node doesn't exist" unless self.nodes.key?(id)

    neighbors_set = Set.new
    self.nodes[id].neighbors.each do |to_id, to_ptr|
      neighbors_set.add(to_id)
    end

    return neighbors_set
  end
end
