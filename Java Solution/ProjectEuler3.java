public class ProjectEuler3{

    public static void main(String[] args){

        long number = 600851475143L;
        int i = 3, maxDivisor = 0;

        while(true){

            while(number % i == 0){

                number /= i;
                maxDivisor = i;
            }

            if (number == 1) break;
            i += 2;

        }

        System.out.println(maxDivisor);

    }
}