import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class DataSet {
    List<Double> numbers = new ArrayList<>();
    public void add(double value) {
        numbers.add(value);
    }

    public double getAverage() {
        double sum = 0;
        int count = 0;
        for (double i : numbers) {
            sum += i;
            count++;
        }
        return sum / count;
    }

    public double getSmallest() {
        Collections.sort(numbers);
        return numbers.get(0);
    }

    public double getLargest() {
        Collections.sort(numbers);
        return numbers.get(numbers.size()-1);
    }

    public double getRange() {
        Collections.sort(numbers);
        return (numbers.get(numbers.size()-1)) - numbers.get(0);
    }
}
