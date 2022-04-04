import java.util.ArrayList;
import java.util.List;

public class DataSet {
    List<Double> numbers = new ArrayList<>();
    public void add(double value) {numbers.add(value);}

    public double getAverage() {
        int count = 0;
        double sum = 0;
        for (double i : numbers) {
            sum += i;
            count++;
        }
        return sum / count;
    }

    public double getStandardDeviation() {
        double sumOfSquares = 0;
        for (double i : numbers) {
            sumOfSquares += ( (i - getAverage()) * (i - getAverage()) );
        }
        double count = 0;
        for (double i : numbers) { count++; }
        return Math.sqrt(sumOfSquares / (count - 1));
    }
}
