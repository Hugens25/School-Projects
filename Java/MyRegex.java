import java.util.*;

public class MyRegex
{
  public static void main(String args[])
  {
    String pattern = "((25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)(.)){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?){1}";
    Scanner scan = new Scanner(System.in);
    String line = "";
    while(scan.hasNext())
    {
      line = scan.nextLine();
      System.out.printf(!line.matches(pattern)?"\n"+line+" is not a pattern": "\n"+line+" is a pattern");
    }
  }
}
