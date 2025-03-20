public class BubbleSort {
    public void sort(int[] array) {
        boolean isSorted;
        for (int i = 0; i < array.length - 1; i++) {
            isSorted = true;
            for (int j = 0; j < array.length - i - 1; j++)
                if (array[j] > array[j + 1]){
                    swap(array, j, j + 1);
                    isSorted = false;
                }
            if (isSorted)
                return;
        }
    }

    private void swap(int[] array, int index1, int index2) {
        int temp = array[index1];
        array[index1] = array[index2];
        array[index2] = temp;
    }
}
