import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Subtasks4 {
    public static void main(String[] args) {
        String inputPath = "input.txt";
        String outputPath = "output.txt";
        
        try (BufferedReader reader = new BufferedReader(new FileReader(inputPath));
             BufferedWriter writer = new BufferedWriter(new FileWriter(outputPath))) {
            
          
            int n = Integer.parseInt(reader.readLine());
            int x = (n + 1) / 2; 
            
           
            for (int i = 1; i <= x; i++) {
               
                writer.write(" ".repeat((n - i) - 1));  
               
                writer.write("*".repeat(2 * i - 1));    
                writer.newLine();
            }
            
            
            for (int i = x - 1; i > 0; i--) {
               
                writer.write(" ".repeat((n - i) - 1));  
               
                writer.write("*".repeat(2 * i - 1));    
                writer.newLine();
            }
            
        } catch (IOException e) {
            e.printStackTrace(); 
        }
    }
}