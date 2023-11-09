package dsa_notes.dsa_notes.data_structures.ArrayListJ;
public class MyArrayList<T> {
    private Object[] backingStruct;
    private int size;
    private final int DEFAULT_CAPACITY = 10;
    public MyArrayList() {
        this.backingStruct = new Object[DEFAULT_CAPACITY];
        this.size = 0;
    }
    public int size() {
        return size;
    }
    public void add(Object value) {
        add(size, value);
    }
    public void add(int index, Object value) {
        if (index < 0 || index > size) {
            throw new IndexOutOfBoundsException();
        }
        if (size >= backingStruct.length) {
            Object[] resized = new Object[backingStruct.length*2];
            for (int i=0; i<size; i++) {
                resized[i] = backingStruct[i];
            }
            backingStruct = resized;
        }
        for (int i=size; i>index; i--) {
            backingStruct[i] = backingStruct[i-1];
        }
        backingStruct[index] = value;
        size++;
    }
    public void remove(Object value) {
        remove(value, false);
    }
    public void remove(Object value, boolean all) {
        int index = 0;
        while (index < size) {
            if (backingStruct[index] == value) {
                for (int i=index; i<size; i++) {
                    backingStruct[i] = backingStruct[i+1];
                }
                size--;
                if (!all) break;
            } else {
                index++;
            }
        }
    }
    public String toString() {
        String result = "[";
        for (int i=0; i<size; i++) {
            result += backingStruct[i] + ", ";
        }
        result = result.substring(0, result.length()-2) + "]";
        return result;
    }
}
