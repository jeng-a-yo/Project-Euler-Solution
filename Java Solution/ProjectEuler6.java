public class ProjectEuler6{

    public static void main(String[] args){

        long sum1 = 0, sum2 = 0;

        for (int i = 1;i <= 100; i++){
            sum1 += i * i;
        }

        for (int i = 1;i <= 100; i++){
            sum2 += i;
        }

        sum2 = sum2 * sum2;

        System.out.println(sum2 - sum1);

    }

}