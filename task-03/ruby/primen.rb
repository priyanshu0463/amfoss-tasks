print "Enter the number: "
x = gets.chomp.to_i

(2..x).each do |i|
    f = 0
    (2..i-1).each do |j|
        if i % j == 0
            f = 1
            break
        end
    end

    if f == 0
        puts "#{i}: prime"
    end
end
