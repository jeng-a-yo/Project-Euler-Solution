public class ProjectEuler2{
    public static void main(String[] args){
        
        int sum = 0;

        int pre = 1, cur = 1, next = 2;

        while(cur < 4000000){
            if (cur % 2 == 0){
                sum += cur;
            }
            pre = cur;
            cur = next;
            next = pre + cur;

        }

        System.out.println(sum);

    }
}