import java.util.ArrayList;
import java.util.Scanner;

public class treesales{
  public static void main(String args[]){
    ArrayList list = new ArrayList<Node>();
    Scanner in = new Scanner(System.in);
    int numCompanies = in.nextInt();

    for(int i = 0; i < numCompanies; i++){
      int numOperations = in.nextInt();
      for(int j = 0; j < numOperations; j++){
        String operation = in.nextLine();
        String [] componentsOfOperation = operation.split(" ");
        switch(componentsOfOperation[0]){
          case "ADD":
            if (componentsOfOperation[1] == "ROOT"){
              list.add(new Node(componentsOfOperation[2]));
            }
            else{
              for (Object element : list){
                if (element.name.equals(componentsOfOperation[1])){
                  element.add(new Node(componentsOfOperation[2]));
                }
              }
            }
        }
      }
    }
  }
}

class Node{
  String name;
  int sale;
  ArrayList children = new ArrayList<Node>();

  public Node(String name){
    this.name = name;
  }
  public void add(Node node){
    children.add(node);
  }

  public int sale(Node node){
    return this.sale;
  }

  public int query(Node node){
    return this.sale;
  }
}
