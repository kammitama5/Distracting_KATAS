function meepOut(quote) {
    quote = quote.replace(/meep/g, "beep")
    quote = quote.replace(/Meep/g, "Beep")
    //console.log(quote)
    return quote
}
