import java.util.Scanner;

public class Sum {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        int[] array = new int[t];
        for (int i : array) {
            array[i] = scan.nextInt();
        }
        int sum = add(array);
        System.out.println("The sum of the array elements is : " + sum);
    }

    public int add(int[] nums) {
        int sum = 0;
        for (int i : nums) {
            sum += nums[i];
        }
        return sum;
    }
}