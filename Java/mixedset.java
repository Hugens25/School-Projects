import java.util.*;
import java.io.*;

public class mixedset{

  public static void main(String []args)
  {

    Scanner in = new Scanner(System.in);
    int num_cases = in.nextInt();

    for (int i = 0; i < num_cases; i++)
    {
      int n = in.nextInt();
      int s = in.nextInt();
      int k = in.nextInt();

      int[] arr = new int[n];

      for(int j = 0; j < n; j++)
      {
        arr[j] = j+1;
      }
      permuteHelper(arr, 0, n, s, k);
    }
  }

  private static void permuteHelper(int[] arr, int index, int n, int s, int k){
    if(index >= s - 1){ //If we are at the last element - nothing left to permute
      System.out.println(Arrays.toString(arr));

      return;
    }

    for(int i = index; i < s; i++){ //For each index in the sub array arr[index...end]

      //Swap the elements at indices index and i
      int t = arr[index];
      arr[index] = arr[i];
      arr[i] = t;

      //Recurse on the sub array arr[index+1...end]
      if(index+1 <= s)
        permuteHelper(arr, index+1, n, s, k);

      //Swap the elements back
      t = arr[index];
      arr[index] = arr[i];
      arr[i] = t;
    }
  }
}
