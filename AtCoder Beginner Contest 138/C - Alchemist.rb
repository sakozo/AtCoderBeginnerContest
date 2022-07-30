n = gets.to_i
nums = [0]
nums =gets.chomp.split(" ").map(&:to_i);

nums = nums.sort
i = 2.0

sum = 0.0
sum = (nums[0] + nums[1])/2.0

#puts sum

if n >= 3 
	while i <=  n-1 do
		sum = (sum + nums[i])/2.0
		i = i + 1
	end
end

puts sum
