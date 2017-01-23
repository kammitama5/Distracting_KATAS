function sentenceCount(string) {
      console.log(string)
      a = (string.split(".").length - 1)
      b = (string.split("?").length - 1)
      c = (string.split("!").length - 1)
      return (a + b + c)
      
}
