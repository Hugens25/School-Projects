public class LatticePaths
{
  public static void main (String args[])
  {
    int num = 2, i = 0, j = 0, a = 0;
    Element[][] array = new Element[num + 1][num + 1];

    for(i = 0; i < num + 1; i++)
    {
      for (j = 0; j < num + 1; j++)
      {
        array[i][j].right = 0;
        array[i][j].down = 0;

        if(i == num)
        {
          array[i][j].down = 1;
        }
        if(j == num)
        {
          array[i][j].right = 1;
        }
      }
    }

    for(a = 0; a < num; a++)
    {
      i = 0;
      j = 0;
      while(array[i][j].right != 1)
      {

      }
    }
  }
}

class Element
{
  int right;
  int down;

  public Element(int a, int b)
  {
    right = a;
    down = b;
  }

}
