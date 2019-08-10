class MySet
{
  int[] arr = new int[1];

  public void insert(int val)
  {
    if (arr.length == 0){
      arr[0] = val;
      return;
    }

    for(int i = 0; i < this.arr.length; i++)
    {
      if(val == this.arr[i])
        return;
      if(this.arr[i] == 0){
        arr[i] = val;
        return;
      }

      if(i == this.arr.length-1){
        this.arr = resize(arr);
        this.arr[i+1] = val;
        return;
      }
    }
  }

  public int[] resize(int[] arr){
    int[] newArr = new int[arr.length*2];
    for(int i = 0; i < arr.length; i++)
    {
      newArr[i] = arr[i];
    }
    return newArr;
  }

  public void printMe(){
    String str = "";
    for(int val: this.arr)
    {
      str+= val+" ";
    }
    System.out.println(str);
  }
}

public class set
{
  public static void main(String args[])
  {
    MySet thisSet = new MySet();
    thisSet.insert(1);
    thisSet.insert(2);
    thisSet.insert(3);
    thisSet.insert(4);
    thisSet.insert(5);
    thisSet.insert(6);
    thisSet.insert(7);
    thisSet.printMe();
  }
}
