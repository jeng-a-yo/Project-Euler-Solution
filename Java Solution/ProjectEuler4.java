public class ProjectEuler4{

    public static boolean IsPalindrome(int number){

        int reverse = 0, temp = number;

        while (temp != 0){

            reverse *= 10;
            reverse += temp % 10;
            temp /= 10;

        }

        return number == reverse;

    }

    public static void main(String[] args){

        int maxNumber = 0;

        for (int i = 100; i < 999; i++){
            for (int j = i + 1; j < 999; j++){
                if (IsPalindrome(i * j) && (i * j) > maxNumber) maxNumber = i * j;
            
            }
        }

        System.out.println(maxNumber);

    }
}