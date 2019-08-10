import java.io.*;
import java.util.*;

public class HR_StringToken {

    public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      String s = scan.nextLine();
      s = s.trim();
      String [] stringArray = s.split("[\\W+\\s+^!^,^?^.^_^'^@]+");
      int sLength = stringArray.length;
      System.out.println(sLength >= 0? sLength : "0");

      for(int i = 0; i < sLength; i++)
          System.out.println(stringArray[i]);
      scan.close();
    }
}
