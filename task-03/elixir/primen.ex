IO.puts("Enter a number:")
x = String.to_integer(IO.gets(""))

for i <- 2..x do
  f = 0

  for j <- 2..(i-1) do
    if rem(i, j) == 0 do
      f = 1
      
    end
  end

  if f == 0 do
    IO.puts("#{i} : Prime")
  end
end
