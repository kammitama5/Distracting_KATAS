function sumLength (arr){
    var count = 0
    var sum = 0
		if (arr.length == 0){
		  return "0 0"
		}
		else{
		  for (var i = 0; i <= arr.length; i++){
		    if (arr[i] < 0){
		      count = count + 1
		      
		    }
		    else if (arr[i] > 0){
		      sum = sum + arr[i]
		    }
		  }
		  
		}

		console.log(sum.toString() + " " + count.toString())
    return ;
}


sumLength([1,2,3,4,-1,-2,-3])//, '10 3')
sumLength([1,2,3,4,0,-1,-2,-3])//, '10 4')
sumLength([-1,2,3,4,0,1,0,-2,0,-3])//, '10 5')
//sumLength([-1,-2,-3,-4,0,-1,0,-2,0,-3])//, '0 9')
//sumLength([1,2,3,4,1,2,3])//, '16 0')
//sumLength([0,0,0,0,0,0,0])//, '0 4')
//sumLength([])//, '0 0')

