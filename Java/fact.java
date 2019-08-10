import java.util.*;
import java.io.*;
import java.lang.*;

public class fact
{
  static ArrayList isPrime = new ArrayList<Integer>();

  public static void main(String args[])
  {
    isPrime.add(1);
    sieve(7920);

    Scanner in = new Scanner(System.in);
    int numCases = Integer.parseInt(in.nextLine());
    int num, val, start=0, k=0;
    for(int i = 0; i < numCases; i++)
    {
      num = Integer.parseInt(in.nextLine());
      while(isPrime.get(k+1) < num)
      {
        start = isPrime.get(k);
        k++;
      }
      while(num > 0)
      {
        for(k; k > 0; k--)
        {
          if(num % isPrime.get(k) == 0)
          {
            val += Math.floor(num / );
          }
        }
      }
    }
  }

  public static void sieve(int n)
  {

    for(int i = 2; i < n; i++)
    {
      boolean numIsPrime = true;
      for(int j = 2; j <= Math.sqrt(i); j++)
      {
        if(i % j == 0)
        {
          numIsPrime = false;
          break;
        }
      }
      if(numIsPrime)
        isPrime.add(i);
    }
  }
}
