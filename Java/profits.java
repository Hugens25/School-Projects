import java.util.*;
import java.io.*;

public class profits
{
  public static void main(String args[])
  {

    Scanner in = new Scanner(System.in);
    ArrayList list = new ArrayList<>();

		int numCases=1;

    while(numCases != 0)
    {
      try
      {
        numCases = Integer.parseInt(in.nextLine());
        // if(numCases == 0)
        //   break;
      }
      catch(Exception e)
      {
        numCases = 0;
      }
      int max=0, sum=0, start=0, end=0, i=0;
  		for (int j=0; j<numCases; j++)
      {
        try
        {
  			  sum += Integer.parseInt(in.nextLine());
        }
        catch(Exception e)
        {
          sum += 0;
        }
        if(j == 0)
          max = sum;

  			// Update if we get a better max.
  			if (sum > max)
        {
  				max = sum;
  				start = i;
  				end = j;
  			}

  			// If our running sum falls below 0, there's no need to
  			// consider it at all, reset the sum to 0.
  			else if (sum < 0)
        {
  				i = j+1;
  				sum = 0;
  			}
  		}
      list.add(max);
    }
    for(int k = 0; k < list.size(); k++)
      System.out.println(list.get(k));

  }
}
