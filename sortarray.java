public class SortArray{

  public static int[] sortArray(int[] ar){
   boolean swapped = true;
    int j = 0;
    int tmp;
    while (swapped) {
        swapped = false;
        j++;
        for (int i = 0; i < ar.length - j; i++) {
            if (ar[i] > ar[i + 1]) {
                tmp = ar[i];
                ar[i] = ar[i + 1];
                ar[i + 1] = tmp;
                swapped = true;
            }
        }
    }
    return ar;
  }
}

