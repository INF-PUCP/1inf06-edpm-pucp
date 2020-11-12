require "set"
require_relative "./graph.rb"

def PrintNodes nodes
  print "Nodes: "
  nodes.each  do |node|
    print " #{node}"
  end
  puts ""
end

# Retorna un mapa con <nodo, distancia minima de raiz a nodo>
def BFS grafo, raiz
  nodos = grafo.GetNodeSet
  infinito = grafo.Size

  distancia = Hash.new
  visitado = Hash.new

  nodos.each do |nodo|
    distancia[nodo] = infinito
    visitado[nodo] = false
  end

  distancia[raiz] = 0
  visitado[raiz] = true
  tour = Queue.new
  tour.push(raiz)

  while not tour.empty? do
    desde = tour.pop
    vecinos = grafo.GetNeighbors(desde)
    vecinos.each do |hacia|
      if not visitado[hacia]
        distancia[hacia] = distancia[desde] + 1
        visitado[hacia] = true
        tour.push(hacia)
      end
    end
  end

  return distancia
end

def ImprimirDistanciasMinimas distancias, raiz
  infinito = distancias.size
  puts "Distancias minimas desde #{raiz}:"
  distancias.each do |destino, distancia|
    print "d(#{raiz}, #{destino}) = ";
    if distancia < infinito
      puts "#{distancia}"
    else
      puts "oo"
    end
  end
end

graph = Graph.new

graph.AddEdge(0, 2)
graph.AddEdge(0, 5)
graph.AddEdge(1, 6)
graph.AddEdge(2, 6)
graph.AddEdge(3, 4)
graph.AddEdge(4, 5)
graph.AddEdge(5, 3)
graph.AddEdge(5, 7)
graph.AddEdge(7, 2)
graph.AddEdge(7, 8)

distancias_minimas = BFS(graph, 0)
ImprimirDistanciasMinimas(distancias_minimas, 0)
