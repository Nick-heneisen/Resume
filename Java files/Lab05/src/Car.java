public class Car {
    private double efficiency;
    private double fuel;

    public Car(double specificEfficiency){
        this.efficiency=specificEfficiency;
        this.fuel=0;
    }
    public void drive(double distance){
        this.fuel=this.fuel-(distance/this.efficiency);
    }
    public double getGasInTank(){
        return this.fuel;
    }
    public void addGas(double gasoline){
        this.fuel=gasoline+this.fuel;
    }
}