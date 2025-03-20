import java.util.Arrays;

public class MergeSort {
    public void sort(int[] array) {
        if (array.length < 2)
            return;

        var mid = array.length / 2;
        var left = Arrays.copyOfRange(array, 0, mid);
        var right = Arrays.copyOfRange(array, mid, array.length);

        sort(left);
        sort(right);

        merge(left, right, array);
    }

    private void merge(int[] left, int[] right, int[] result) {
        int i = 0, j = 0, k = 0;
        while (i < left.length && j < right.length){
            if (left[i] < right[j])
                result[k++] = left[i++];
            else
                result[k++] = right[j++];
        }

        while (i < left.length)
            result[k++] = left[i++];

        while (j < right.length)
            result[k++] = right[j++];
    }
}
