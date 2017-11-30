function celsiusToFahrenheit(celsius) {
  if (typeof(celsius) === "number")
  {
    var fahrenheit = (celsius * (9.0/5)) + 32.0
    return fahrenheit;
  }
  else
  {
    return undefined;
  }
}

