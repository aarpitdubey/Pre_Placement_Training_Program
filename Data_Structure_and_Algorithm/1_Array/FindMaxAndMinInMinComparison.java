public class FindMaxAndMinInMinComparison {

    static int[] getMinMax(int arr[], int n) 
{
    int i;
    int max = 0, min = 0;

    // If array is an empty array

    if (n == 0) {
        return new int[]{max, min};
    }

    // If only one element in the array

    if(n == 1) 
    {
        max = arr[0];
        min = arr[0];
        return new int[]{max, min};
    }

    // if there are more than one elements

    if(arr[0] > arr[1])
    {
        max = arr[0];
        min = arr[1];
        return new int[]{max, min};
    }

    for(i = 2; i < n; i++)
    {
        if(arr[i] > max){
            max = arr[i];
        } else if(arr[i] < min) {
           min = arr[i];
        }
    }

    return new int[]{max, min};
}

public static void main(String[] args) {
    int arr[] = {3, 5, 4, 1, 9};
    int arr_size = 5;
    int [] minmax = getMinMax(arr, arr_size);
    System.out.printf("\nMinimum element is %d\n",minmax[1]);
    System.out.printf("\nMaximum element is %d\n\n",minmax[0]);
}
}