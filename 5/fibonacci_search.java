public class fibonacci_search {

    public static int fibSearch(int[] arr, int x) {
        int n = arr.length;
        int fib2 = 0;
        int fib1 = 1;
        int fib = fib2 + fib1;

        while (fib < n) {
            fib2 = fib1;
            fib1 = fib;
            fib = fib2 + fib1;
        }

        int offset = -1;

        while (fib > 1) {
            int i = Math.min(offset + fib2, n - 1);

            if (arr[i] < x) {
                fib = fib1;
                fib1 = fib2;
                fib2 = fib - fib1;
                offset = i;
            } else if (arr[i] > x) {
                fib = fib2;
                fib1 = fib1 - fib2;
                fib2 = fib - fib1;
            } else {
                return i;
            }
        }

        if (fib1 == 1 && offset + 1 < n && arr[offset + 1] == x)
            return offset + 1;

        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100};
        int x = 85;

        System.out.print("Массив: ");
        for (int n : arr) System.out.print(n + " ");
        System.out.println();

        int result = fibSearch(arr, x);
        if (result != -1)
            System.out.println("Элемент " + x + " найден на позиции " + result);
        else
            System.out.println("Элемент " + x + " не найден");
    }
}
