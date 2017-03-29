function bmi(w, h) {
      var bmi = w / (h * h)
      if (bmi <= 15){
        return("Very severely underweight")
      }
      else if (bmi <= 16){
        return("Severely underweight")
      }
      else if (bmi <= 18.5){
        return("Underweight")
      }
      else if (bmi <= 25){
        return("Normal (healthy weight)")
      }
      
      else if (bmi <= 30){
        return("Overweight")
      }
      else if (bmi <= 35){
        return("Moderately obese")
      }
      else if (bmi <= 40){
        return("Severely obese")
      }
      else if (bmi > 40){
        return("Very severely obese")
      }
}

