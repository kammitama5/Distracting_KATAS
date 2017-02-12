
function sumLength (arr){
    total = 0 
    count = 0
		if (arr == []){
		  return('0 0')
		}
		else{
		  for (var i =0; i < arr.length; i++){
		    if (arr[i] < 0){
		      count = count + 1
		    }
		    else if (arr[i] == 0){
		      count = (count + 1/2.0)
		    }
		    else{
		      total = total + arr[i]
		    }
		  }
		}
		return(total.toString() + " " + count.toFixed())
}
