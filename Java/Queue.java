import java.util.PriorityQueue;

public class Queue{

  public static void main(String args[]){
    PriorityQueue pQueue = new PriorityQueue<Employee>();
    Employee Hugh = new Employee("Hugh", 25, 1);
    Employee Jess = new Employee("Jess", 23, 2);
    Employee Empty = new Employee("Empty", 0, 3);
    pQueue.add(Hugh);
    pQueue.add(Jess);
    pQueue.add(Empty);

    System.out.println(pQueue);
    while(!pQueue.isEmpty()){
      System.out.println(pQueue.poll());
    }

  }

}

class Employee implements Comparable<Employee>{
  String name;
  int age;
  int emplId;

  public Employee(String name, int age, int emplId){
    this.name = name;
    this.age = age;
    this.emplId = emplId;
  }

  public int compareTo(Employee other){
    if (this.emplId == other.emplId)
      return 0;

    if (this.emplId > other.emplId)
      return -1;

    else
      return 1;

  }

  public String toString(){
    return this.name;
  }

}
