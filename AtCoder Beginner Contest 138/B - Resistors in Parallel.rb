n = gets.to_i

nums = []
nums = gets.chomp.split(" ").map(&:to_i);

sum = 0.0

for i in 0..n-1 do 
	#puts (1.0/nums[i])
	sum = sum + (1.0/nums[i])
end

puts 1/sum