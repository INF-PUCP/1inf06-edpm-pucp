# Retorna a^b (mod p) en O(lg(b))
def Exponenciacion(a, b, p)
  resultado = 1
  while b > 0 do
    if b % 2 == 1
      resultado = (resultado * a) % p
    end
    a = (a * a) % p
    b = b / 2
  end
  return resultado
end

# Retorna un inverso modular x tal que a * x = 1 (mod p)
# Complejidad en tiempo: O(lg(p))
# Utilizamos el pequeño Teorema de Fermat
# a^(p - 1) = 1 (mod p)
# a^(p - 2) = a^(-1) (mod p)
def InversoModular(a, p)
  return Exponenciacion(a, p - 2, p)
end

print "Ingrese un numero primo: "
p = gets.chomp  # Lectura de string desde standar input sin el salto de linea
p = p.to_i  # Convertimos el string a entero

# Calculare los inversos modulares de los numeros que ingresen hasta recibir -1
while true do
  print "Ingrese un numero en [1,#{p - 1}] o -1 para terminar: "
  x = gets.chomp
  x = x.to_i
  if x == -1
    break
  end
  inv = InversoModular(x, p)
  puts "#{inv} es el inverso modular de #{x}, pues #{x} * #{inv} = 1 (mod #{p})"
end

puts "Fin del programa. Gracias."
