public class ProjectEuler10 {

    public static boolean IsPrime(int number){

        if (number % 2 == 0) return false;

        for (int i = 3; i * i <= number; i += 2){

            if (number % i == 0) return false;

        }

        return true;

    }

    public static void main(String[] args){

        long sum = 2;

        for (int i = 3; i < 2000000; i += 2){

            if (IsPrime(i)) sum += i;

        }

        System.out.println(sum);

    }

}