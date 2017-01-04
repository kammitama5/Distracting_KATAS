function smallestPairSum(numbers)
{
    c = numbers.sort((a, b) => a - b);
    sum = c[1] + c[0]
    return sum
}
