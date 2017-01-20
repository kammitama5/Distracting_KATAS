function calcRun(miles, caloriesPerMile) {    
          var totm = miles * caloriesPerMile
          var totc = totm / 2300.00
          var cost = (1.75 * totc)
          return Number(cost.toFixed(2))
}
