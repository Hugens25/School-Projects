/*
ID: hugens21
LANG: Java
PROG: ride
*/

import java.util.*;
import java.io.*;

public class Ride
{
  public static void main(String args[])
  {
    Scanner in = new Scanner(System.in);
    String word;
    int total, j;
    ArrayList list = new ArrayList<Integer>();

    while(in.hasNext())
    {
      j = 0;
      word = in.nextLine().toLowerCase();
      total = 1;
      for(int i = 0; i < word.length(); i++)
      {
        total *= Character.getNumericValue(word.charAt(i)) - 9;
      }
      list.add(total);
      System.out.println(total);
    }
    System.out.println(((int)list.get(0) % 47 == (int)list.get(1) % 47) ? "GO" : "STAY");
    list.clear();
  }
}
