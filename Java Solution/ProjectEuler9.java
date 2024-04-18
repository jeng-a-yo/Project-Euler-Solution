public class ProjectEuler9{

    public static void main(String[] args){

        for (int i = 0; i < 999; i++) {
            for (int j = 0; j < 999; j++) {
                for (int k = 0; k < 999; k++) {
                    if ((j * j + k * k == i * i) && (i + j + k == 1000)){
                        System.out.println(i * j * k);
                        return;
                    }
                }
            }

        }

    }

}