public class RomanNums{
  public static void main (String [] args){
    String str = args[0];
    int num = 0;

    for (int i = str.length() - 1; i >= 0; i--){
      num += value(str.charAt(i));
      if (i > 0 && (num == 5 || num == 10)){
        if (value(str.charAt(i - 1)) == 1){
          num -= 1;
          i -= 1;
        }
      }
      if (i > 0 && (num == 50 || num == 100)){
        if (value(str.charAt(i - 1)) == 10){
          num -=10;
          i -= 1;
        }
      }
    }
    System.out.println(str+" : "+num);
  }

  public static int value(char c){
    if (c == 'I'){
      return 1;
    }
    if (c == 'V'){
      return 5;
    }
    if (c == 'X'){
      return 10;
    }
    if (c == 'L'){
      return 50;
    }
    if (c == 'C'){
      return 100;
    }
    return 0;
  }
}
