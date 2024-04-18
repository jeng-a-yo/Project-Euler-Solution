public class ProjectEuler5{

    public static int GCD(int x, int y){

        if (x > y) return GCD(y, x);
        if (y % x == 0) return x;
        return GCD(x, y % x);

    }

    public static int LCM(int x, int y){
        return x * (y / GCD(x, y));
    }

    public static void main(String[] args){

        int multiple = 1;

        for (int i = 2; i <= 20; i++){
            multiple = LCM(i, multiple);
        }

        System.out.println(multiple);

    }

}