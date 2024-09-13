import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Subtask2 {
    public static void main(String[] args) {
        String inputPath = "/home/rijin-rajeevan/amFOSS/task 3/JAVA/input.txt";
        String outputPath = "/home/rijin-rajeevan/amFOSS/task 3/JAVA/output.txt";
        
        try (BufferedReader reader = new BufferedReader(new FileReader(inputPath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                try (BufferedWriter writer = new BufferedWriter(new FileWriter(outputPath, true))) {
                    writer.write(line);
                    writer.newLine();
                } catch (IOException e) {
                    e.printStackTrace(); 
                }
            }
        } catch (IOException e) {
            e.printStackTrace(); 
        }
    }
}
