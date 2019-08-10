public class Main
{
  public static void main (String args[])
  {
    House house1 = new House(red);
    System.out.println("house1 color: "+house1.color);

    House house2 = new House(blue);
    System.out.println("house2 color: "+house2.color);

    House house3 = house1;
    System.out.println("house3 color: "+house3.color);

    System.out.println("\nChanging House3 color...\n");
    house3.color = yellow;

    System.out.println("house1 color: "+house1.color);
    System.out.println("house3 color: "+house3.color);
  }

}
