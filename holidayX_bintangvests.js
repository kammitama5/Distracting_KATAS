function vestBuy(price, haggle)
{
    if (haggle == "light"){
      return(.80 * price)
    }
    else if (haggle == "medium"){
      return(.70 * price)
    }
    else if (haggle == "heavy"){
      return(.60 * price)
    }
    else if (haggle == "walkandswear"){
      return(.10 * price)
    }
    else{
      return("Run!!")
    }
    return
}
