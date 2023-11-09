package dsa_notes.dsa_notes.data_structures.ArrayListJ;
public class Client {
    public static void main(String[] args) {
        System.out.println("My Array List Test!");
        MyArrayList<Integer> myList = new MyArrayList<>();
        myList.add(1);
        myList.add(2);
        myList.add(3);
        myList.add(3);
        myList.add(3);
        myList.add(4);
        myList.add(5);
        System.out.println(myList);
        myList.remove(5);
        System.out.println(myList);
        myList.remove(3, true);
        System.out.println(myList);

        MyArrayList<Vehicle> myVehicleList = new MyArrayList<>();
        for (int i=0; i<6; i++) {
            myVehicleList.add(new Vehicle(i, i/2.5));
        }
        System.out.println(myVehicleList);
    }
}
