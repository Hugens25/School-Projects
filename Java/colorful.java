import java.util.*;
import java.io.*;
import java.lang.*;

public class colorful
{
  public static void main(String args[])
  {
    Scanner in = new Scanner(System.in);
    int numVals = in.nextInt();
    //System.out.println("numVals: "+numVals);
    int[] allMax = new int[numVals];
    int[] maxVals = new int[numVals];

    String vals = Integer.toString(in.nextInt());

    for(int i = 0; i < numVals-1; i++)
    {
      vals += Integer.toString(in.nextInt());
    }

    for(int j = 0; j < vals.length(); j++)
    {
      
    }


  }

  public int lastColorDiff(String s, int c)
  {
    for(int i = s.length()-1; i > 0; i--)
    {
        if(Integer.parseInt(s.charAt(i)) != c)
          return i;
    }
  }
}
