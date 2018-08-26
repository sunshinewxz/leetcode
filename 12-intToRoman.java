/*
There will be too many comparisons if using addition and subtraction.
*/
public class Main {
    public static void main(String[] args){
        int num = 1994;
        String result = intToRoman(num);
        System.out.println(result);
    }


    public static String intToRoman(int num) {
        String result = "";
        while(num >= 1000){
            result = result + "M";
            num = num - 1000;
        }
        if(num >= 900){
            result = result + "CM";
            num = num - 900;
        }
        if(num >= 500){
            result = result + "D";
            num = num - 500;
        }
        if(num >= 400){
            result = result + "CD";
            num = num - 400;
        }
        if(num >= 100){
            while(num >= 100){
                result = result + "C";
                num = num - 100;
            }
        }
        if(num >= 90){
            result = result + "XC";
            num = num - 90;
        }
        if(num >= 50){
            result = result + "L";
            num = num - 50;
        }
        if(num >= 40){
            result = result + "XL";
            num = num - 40;
        }
        if(num >= 10){
            while(num >= 10){
                result = result + "X";
                num = num - 10;
            }
        }
        if(num >= 9){
            result = result + "IX";
            num = num - 9;
        }
        if(num >= 5){
            result = result + "V";
            num = num - 5;
        }
        if(num >= 4){
            result = result + "IV";
            num = num - 4;
        }
        if(num >= 1){
            while(num >= 1){
                result = result + "I";
                num = num - 1;
            }
        }
        return result;
    }
}

/*
Using quotient method to extract the number on each digit and then represent them separately.
*/
public static String intToRoman(int num) {
        String result = "";
        char roman[] = {'M','D','C','L','X','V','I'};
        int value[] = {1000,500,100,50,10,5,1};

        for(int i=0; i<7; i+=2){
            int x = num/value[i];
            if(x < 4){
                for(int j=0; j<x; j++)
                    result += roman[i];
            }
            else if(x == 4){
                result = result + roman[i] + roman[i-1];
            }
            else if(x < 9){
                result += roman[i-1];
                for(int j=0; j<x-5;j++)
                    result += roman[i];
            }
            else
                result = result + roman[i] + roman[i-2];
            num %= value[i];
        }
        return result;
    }

/*
List every situations and search the table for every digits
However, it takes more time to access to an array
*/
public static String intToRoman(int num) {
        String result = "";
        String v1[] = {"","M","MM","MMM"};
        String v2[] = {"","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"};
        String v3[] = {"","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"};
        String v4[] = {"","I","II","III","IV","V","VI","VII","VIII","IX"};
        result = v1[num/1000] + v2[(num%1000) / 100] + v3[(num%100) / 10] + v4[num%10];
        return result;
    }
/*
Divide the domain and compare.
*/
public static String intToRoman(int num) {
        String result = "";
        int value[] = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
        String roman[] = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        for (int i = 0; i < value.length; i++){
            while(num >= value[i]){
                result += roman[i];
                num -= value[i];
            }
        }
        return result;
    }


/*
Making use of '+' to concate the string uses more time than ".append()"
*/
public static String intToRoman(int num) {
        StringBuilder result = new StringBuilder();
        int value[] = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
        String roman[] = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        for (int i = 0; i < value.length; i++){
            while(num >= value[i]){
                result.append(roman[i]);
                num -= value[i];
            }
        }
        return result.toString();
    }
