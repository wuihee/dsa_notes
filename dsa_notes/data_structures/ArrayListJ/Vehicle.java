package dsa_notes.dsa_notes.data_structures.ArrayListJ;
public class Vehicle {
    private int miles;
    private double mpg;
    public Vehicle(int miles, double mpg) {
        this.miles = miles;
        this.mpg = mpg;
    }
    public String toString() {
        return "Vehicle with " + miles + " miles and " + mpg + " mpg.";
    }
}