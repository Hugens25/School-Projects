import java.util.*;
import java.io.*;
import java.lang.*;

public class perm
{
  public static void main(String args[])
  {
    Scanner in = new Scanner(System.in);
    int num_cases = in.nextInt();
    String [] outputs = new String[num_cases];

    for(int i = 0; i < num_cases; i++)
    {
      String num_set = in.next();
      String val = in.next();
      String begin = "";
      String end = "";
      String compare = "";
      Boolean finish = false;

      for(int j = val.length() - 1; j > 0; j--)
      {
        if (val.charAt(j) > val.charAt(j-1))
        {
          begin += val.substring(0, j-1);
          end += val.substring(j-1, val.length());
          compare += Character.toString(end.charAt(0));
          //System.out.println("Begin: "+begin+" End: "+end+" Compare: "+compare);
          break;
        }
        if(j - 1 == 0)
        {
          System.out.println("BIGGEST");
          finish = true;
        }
      }
      if(!finish)
      {
        String str = end.substring(1, end.length());
        char [] strArray = str.toCharArray();
        Arrays.sort(strArray);
        str = Arrays.toString(strArray).replace("[", "").replace("]", "").replace(",","").replace(" ","");
        for(int k = 0; k < str.length(); k++)
        {
          if(str.charAt(k) >= compare.charAt(0))
          {
            begin += Character.toString(str.charAt(k));
            //System.out.println("Str after begin add: "+begin);
            //System.out.println("Compare: "+compare);
            str += compare;
            //System.out.println("str: "+str);
            String concatStr = str.substring(0,k)+str.substring(k+1,str.length());
            char [] conStrArray = concatStr.toCharArray();
            Arrays.sort(conStrArray);
            concatStr = Arrays.toString(conStrArray).replace("[", "").replace("]", "").replace(",","").replace(" ","");
            //System.out.println("sub(0,k): "+concatStr.substring(0,k));
            //System.out.println("sub(k,length): "+concatStr.substring(k+1,concatStr.length()));
            //System.out.println("conSTR: "+concatStr);
            begin += concatStr;
            break;
          }
        }
      }
      if(!finish)
        System.out.println(begin);
    }
  }
}
