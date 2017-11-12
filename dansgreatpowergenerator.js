function danspower(num, power) {
    var power1 = Math.pow(num, power)
    if (power1 % 2 == 0)
    {
      return power1
    }
    else
    {
      return (Math.round(power1 / 10) * 10);
    }
}
