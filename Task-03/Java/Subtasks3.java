import java.util.*;
public class  Subtasks3{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("enter no. of rows :");
        int row =sc.nextInt();
        int x = Math.floorDiv(row,2);
        for(int i =1;i<=x+1;i++){
            for(int j =1;j<=(row-i)-2;j++){
                System.out.print(" ");
            }
            for(int j =1;j<=(2*i)-1;j++){
                System.out.print("*");
            }
            System.out.println();
        }
        for(int i= x;i>=0;i--){
            for(int j =1;j<=(row-i)-2;j++){
                System.out.print(" ");
            }
            for(int j =1;j<=(2*i)-1;j++){
                System.out.print("*");
            }
            System.out.println();
        }
        
        sc.close();       
        
    }
  }
