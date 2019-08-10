import java.util.ArrayDeque;

public class ADeque{
  public static void main(String args[]){
    ArrayDeque aDeque = new ArrayDeque<Employee>();
    Employee Hugh = new Employee("Hugh", 25, 1);
    Employee Jess = new Employee("Jess", 23, 2);
    Employee Empty = new Employee("Empty", 0, 3);

    String[] arr = {"Hello", "World"};

    aDeque.addFirst(Hugh);
    aDeque.addFirst(Jess);
    aDeque.addLast(Empty);

    //System.out.println(aDeque);

    for(String e : arr)
      System.out.println(e);
  }
}

class Employee{
  String name;
  int age;
  int emplId;

  public Employee(String name, int age, int emplId){
    this.name = name;
    this.age = age;
    this.emplId = emplId;
  }

  public String toString(){
    return this.name;
  }
}
