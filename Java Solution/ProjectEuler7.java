public class ProjectEuler7{

    public static boolean IsPrime(int number){

        if (number % 2 == 0) return false;

        for (int i = 3; i * i <= number; i += 2){

            if (number % i == 0) return false;

        }

        return true;

    }

    public static void main(String[] args){

        int count = 1, number = 3;

        while(true){

            if (IsPrime(number)) count++;
            if (count == 10001) break;

            number += 2;

        }

        System.out.println(number);

    }

}