import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public class SumToNAndWriteToFile {
    public static void main(String[] args) {
        int n = 29; 

        try {
            FileWriter fileWriter = new FileWriter("/home/visual/task12/sums.txt");
            PrintWriter printWriter = new PrintWriter(fileWriter);

            int sum = 0;

            for (int i = 1; i <= n; i++) {
                int result = i + i;
                sum += result;
                printWriter.println(i + " + " + i + " = " + result);
            }

            printWriter.println("Sum of all results: " + sum);

            printWriter.close();
            fileWriter.close();

            System.out.println("Sum results have been written to 'sums.txt'.");
        } catch (IOException e) {
            System.out.println("An error occurred while writing to the file: " + e.getMessage());
        }
    }
}
