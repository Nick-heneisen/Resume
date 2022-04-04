public class FactorGenerator {
    int value = 0;

    public FactorGenerator(int numberToFactor) {
        this.value = numberToFactor;
    }

    int nextFactor() {
        int i = 0;
        for (i = 2; ; i++) {
            if (value % i == 0) {
                value = value / i;
                break;
            }
        }
        return i;
    }

    public boolean hasMoreFactors() {
        if (value > 1)
            return true;
        else
            return false;
    }
}