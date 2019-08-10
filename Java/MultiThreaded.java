/*
  Name:<Hugens Ulysse>
  Course: CNT 4714 Spring 2019
  Assignment title: Project 2 – Multi-threaded programming in Java
  Date:  February 17, 2019
  Class:  <name of class goes here>
*/

import java.util.concurrent.Semaphore;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.io.*;
import java.lang.*;

public class MultiThreaded
{
  public static void main(String args[]) throws Exception
  {
    List<Station> stations = new ArrayList<>();
    List<Conveyor> conveyors = new ArrayList<>();

    Scanner in = new Scanner(new File("config.txt"));
    int totalStations = Integer.parseInt(in.nextLine());

    for(int i = 0; i < totalStations; i++)
    {
      conveyors.add(new Conveyor(i));
    }

    for(int i = 0; i < totalStations; i++)
    {
      Conveyor left = conveyors.get(i);
      Conveyor right = null;

      if (i+1 >= totalStations)
      {
        right = conveyors.get(0);
      }
      else
      {
        right = conveyors.get(i+1);
      }

      stations.add(new Station(i, left, right, Integer.parseInt(in.nextLine())));
    }

    for(Station station : stations)
    {
      Thread thread = new Thread(station);
      thread.start();
    }
  }
}

class Conveyor
{
  int id;
  Semaphore semaphore;

  public Conveyor(int n)
  {
    id = n;
    semaphore = new Semaphore(1);
  }

  public void acquire()
  {
    try
    {
      semaphore.acquire();
    }
    catch (Exception e)
    {
      e.printStackTrace(System.out);
    }
  }

  public void release()
  {
    try
    {
      semaphore.release();
    }
    catch (Exception e)
    {
      e.printStackTrace(System.out);
    }
  }
}

class Station implements Runnable
{
  private int id;
  private Conveyor left;
  private Conveyor right;
  private int workload;

  public Station(int id, Conveyor left, Conveyor right, int workload)
  {
    this.id = id;
    this.left = left;
    this.right = right;
    this.workload = workload;

    System.out.println("Station "+this.id+": In-Connection set to conveyor "+this.left.id+"\n");
    System.out.println("Station "+this.id+": Out-Connection set to conveyor "+this.right.id+"\n");
    System.out.println("Station "+this.id+": Workload set. Station "+this.id+" has "+workload+" package groups to move."+"\n");
  }
  public void doWork()
  {
    new Thread(this).start();
  }

  @Override
  public void run()
  {
    while(workload > 0)
    {
      try
      {
        Thread.sleep(1000);
      }
      catch (Exception e)
      {
        e.printStackTrace(System.out);
      }
      left.acquire();
      System.out.println("Routing Station "+id+": granted access to conveyor "+left.id+"\n");

      right.acquire();
      System.out.println("Routing Station "+id+": granted access to conveyor "+right.id+"\n");

      System.out.println("Routing Station "+id+": successfully moves packages on conveyor "+left.id+"\n");
      System.out.println("Routing Station "+id+": successfully moves packages on conveyor "+right.id+"\n");

      workload--;
      System.out.println("Routing Station "+id+": has "+workload+" packages left to move."+"\n");

      left.release();
      System.out.println("Routing Station "+id+": released access to conveyor "+left.id+"\n");

      right.release();
      System.out.println("Routing Station "+id+": released access to conveyor "+right.id+"\n");
    }

    System.out.println("* * Station "+id+": Workload successfully completed. * *"+"\n");

  }
}
