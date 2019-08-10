import java.util.*;
import java.io.*;

class extraset
{
  public static void main(String args[])
  {
    Scanner in = new Scanner(System.in);
    ArrayList<List<String>> list = new ArrayList<>();

    int numGames = Integer.parseInt(in.nextLine().trim());
    for(int i = 0; i < numGames; i++)
    {
      String vals = in.nextLine();
      int numAttributes = Integer.parseInt(vals.split(" ")[0]);
      int numCards = Integer.parseInt(vals.split(" ")[1]);
      int count = 0;

      for(int j = 0; j < numCards; j++)
      {
        list.add(Arrays.asList(in.nextLine().split(" ")));
      }

      for(int k = 0; k < numCards; k++)
      {
        for(int l = k+1; l < numCards; l++)
        {
          ArrayList<String> neededCard = new ArrayList<>();

          for(int m = 0; m < numAttributes; m++)
          {
            ArrayList<String> possibleVals = new ArrayList<>();
            possibleVals.add("0");
            possibleVals.add("1");
            possibleVals.add("2");

            if(list.get(k).get(m).equals(list.get(l).get(m)))
            {
              neededCard.add(list.get(k).get(m));
              //System.out.println("Added to list");
            }
            else
            {
              possibleVals.remove(list.get(k).get(m));
              possibleVals.remove(list.get(l).get(m));
              neededCard.add(possibleVals.get(0));
            }
          }
          if(list.contains(neededCard))
          {
            count ++;
          }
          else
          {
            //System.out.println("DIDNT NEED CARD: "+neededCard+". Current Cards: "+list.get(k)+" :: "+list.get(l));
          }
        }
      }
      System.out.println(count/3);
    }
  }
}
