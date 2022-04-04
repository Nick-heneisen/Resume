import java.math.BigDecimal;

public class Lab04 {
    public static void main(String[] args) {
        Lab04.one();
        Lab04.two();
        Lab04.three();
        Lab04.four();
        Lab04.five();
        Lab04.six();
        Lab04.seven();
        Lab04.eight();
        Lab04.nine();
        Lab04.ten();
        Lab04.eleven();
        Lab04.twelve();
        Lab04.thirteen();
        Lab04.fourteen();
        Lab04.fifteen();
        Lab04.sixteen();
        Lab04.seventeen();
        Lab04.eighteen();
        Lab04.nineteen();
        Lab04.twenty();
        Lab04.twentyone();
        Lab04.twentytwo();
        Lab04.twentythree();
        Lab04.twentyfour();
        Lab04.twentyfive();
        Lab04.twentysix();
        Lab04.twentyseven();
        Lab04.twentyeight();
        Lab04.twentynine();
        Lab04.thirty();
        Lab04.thirtyone();
        Lab04.thirtytwo();
        Lab04.thirtythree();
        Lab04.thirtyfour();
        Lab04.thirtyfive();
        Lab04.thirtysix();
        Lab04.thirtyseven();
        Lab04.thirtyeight();
        Lab04.thirtynine();
        Lab04.fourty();
        Lab04.fourtyone();
        Lab04.fourtytwo();
        Lab04.fourtythree();
        Lab04.fourtyfour();
        Lab04.fourtyfive();
        Lab04.fourtysix();
        Lab04.fourtyseven();
        Lab04.fourtyeight();
        Lab04.fourtynine();
        Lab04.fifty();
        Lab04.fiftyone();
        Lab04.fiftytwo();
    }

    public static void one() {
        System.out.println("1. What does this line of code print: System.out.println(\"+---+\\n| |\\n+---+\")");
        //expected output is printing a square shape
        System.out.println("+---+\n|   |\n+---+");
    }

    public static void two() {
        System.out.println("2. Write code to calculate the following expression with BigDecimal objects: 4.35 * 100");
        //expected result is 435
        BigDecimal a = new BigDecimal("4.35");
        System.out.println(a.multiply(new BigDecimal("100")));
    }

    public static void three() {
        System.out.println("3. Evaluate: 3 - 4 + 5");
        //This should just do the equation from left to right, following PEMDAS.
        System.out.println(3 - 4 + 5);
    }

    public static void four() {
        System.out.println("4. Evaluate: 3 – 4 * 5");
        //This should result in -17, assuming it does the multiplication first.
        System.out.println(3 - 4 * 5);
    }

    public static void five() {
        System.out.println("5. Evaluate: 2 / 3 * 4");
        /*This should result in 0 because these are integers rather than floats/doubles,
         and java will not print decimals because of it. */
        System.out.println(2/3*4);
    }

    public static void six() {
        System.out.println("6. Evaluate: 2 * 3 / 4");
        //This will be 1 because these are integers and java will round down because of it.
        System.out.println(2 * 3 / 4);
    }

    public static void seven() {
        System.out.println("7. Evaluate: 3 % 5");
        /* My guess was 2 because three is 2 lower than 5, but in reality 5 goes into 3 0 times,
        so 3 is the remainder. */
        System.out.println(3 % 5);
    }

    public static void eight() {
        System.out.println("8. Evaluate: -3 % 5");
        // My guess  is -3 due to the same reason as the above question, and the first number determines negativity.
        System.out.println(-3 % 5);
    }

    public static void nine() {
        System.out.println("9. Evaluate: 5 % 3 ");
        // My guess is 2 because the remainder of 3/5 is 2.
        System.out.println(5 % 3);
    }

    public static void ten() {
        System.out.println("10. Evaluate: 5 % -3 ");
        // My guess is 2 again because the first number determines negativity, and 2 is the remainder.
        System.out.println(5 % -3);
    }

    public static void eleven() {
        System.out.println("11. Evaluate: 3 % -5");
        // My guess is 0 because the first number determines negativity, and 5 goes into 3 zero times.
        System.out.println(3 % -5);
    }

    public static void twelve() {
        System.out.println("12. Evaluate: 49 / 17 % 5");
        // My guess is 2 because 49/14 is 2.88 (which is rounded down by java), and 5 goes into 2 zero times.
        System.out.println(49 / 17 % 5);
    }
    public static void thirteen() {
        System.out.println("13. Evaluate: 49 / (17 % 5)");
        // My guess is 24 because 17%5 is 2, and 49/2 rounded down is 24.
        System.out.println(49 / (17 % 5));
    }
    public static void fourteen() {
        System.out.println("14. Evaluate: ('a' + 'b') % 2");
        // My guess is 1 because I think the % might take a and b as 2 because there's 2 letters, and 2 % 2 is 1.
        System.out.println(('a' + 'b') % 2);
        //It appears it is 1 because of ascii values, which I'm not familiar with.
    }
    public static void fifteen() {
        System.out.println("15. Evaluate: false || true");
        // My guess is true, I don't know that || does but I'm guessing it is or, and false or true is true.
        System.out.println(false || true);
    }
    public static void sixteen() {
        System.out.println("16. Evaluate: ! true && false");
        // My guess is false because not true is false, and false and false is false.
        System.out.println(! true && false);
    }
    public static void seventeen() {
        System.out.println("17. Evaluate: ! (true && false)");
        // My guess is true because true and false is false, and not that is true.
        System.out.println(! (true && false));
    }
    public static void eighteen() {
        int n = 3;
        System.out.println("18. Evaluate: n > ++ n");
        // My guess is false because ++ is before the second n, the second n is 4, 3 < 4.
        System.out.println(n > ++ n);
    }
    public static void nineteen() {
        int n = 3;
        System.out.println("19. Evaluate: ++n - n");
        // My guess is 0 because 4 - 4 = 0
        System.out.println(++n - n);
    }
    public static void twenty() {
        int n = 3;
        System.out.println("20. Evaluate: n++ == n++");
        // My guess is false because n is added after it's read, then the second is read before it's added.
        System.out.println(n++ == n++);
    }
    public static void twentyone() {
        int n = 3;
        System.out.println("21. Evaluate: ++n == n++");
        // My guess is true because the first n equals 4, then the second n is 4 because it is read before it's added.
        System.out.println(++n == n++);
    }
    public static void twentytwo() {
        int n = 3;
        System.out.println("22. Evaluate: n++");
        // My guess is 3 because it's read before it's added.
        System.out.println(n++);
    }
    public static void twentythree() {
        int n = 3;
        System.out.println("23. Evaluate: n++");
        // My guess is 4 because it's read after it's added
        System.out.println(++n);
    }
    public static void twentyfour() {
        int n = 3;
        System.out.println("24. Evaluate: (n = n++ - ++n) < 0");
        // My guess is true because n will equal -2, and -2 is less than 0.
        System.out.println((n = n++ - ++n) < 0);
    }
    public static void twentyfive() {
        int n = 3;
        System.out.println("25. What is n now?");
        // My guess is -2 because n++ - ++n = -2.
        System.out.println(n = n++ - ++n);
    }
    public static void twentysix() {
        System.out.println("26. Evaluate: \"1\" + (2 + 3)");
        // My guess is 15 because the number 5 is being put next to the 1, which is a string.
        System.out.println("1" + (2 + 3));
    }
    public static void twentyseven() {
        System.out.println("27. Evaluate: \"1\" + 2 + 3");
        // My guess is 123 because 2 will be added to the 1, then 3 will be added to the 12.
        System.out.println("1" + 2 + 3);
    }
    public static void twentyeight() {
        System.out.println("28. Evaluate: 1 + \"2\" + 3");
        // My guess is also 123 because the 1 is put in front of the 2, then the 3 is after the 2.
        System.out.println(1 + "2" + 3);
    }
    public static void twentynine() {
        System.out.println("29. Evaluate: 1 + 2 + \"3\"");
        // My guess is also 33 because 1 and 2 are added to get 3, then that is put in front of the string.
        System.out.println(1 + 2 + "3");
    }
    public static void thirty() {
        System.out.println("30. \"tomato\".charAt(2) - \"potato\".charAt(5) ");
        // My guess is -2 because m is the 13th letter, and 0 is the 15th letter, 13-15 is -2.
        System.out.println("tomato".charAt(2) - "potato".charAt(5));
    }
    public static void thirtyone() {
        System.out.println("31. \"eggplant\".length()");
        // My guess is that this will be 8 because there's 8 letters.
        System.out.println("eggplant".length());
    }
    public static void thirtytwo() {
        System.out.println("32. \"eggplant\".substring(\"kale\".length())");
        // My guess is that this will say "eggp", because it's the first 4 letters of eggplant.
        System.out.println("eggplant".substring("kale".length()));
        // It said "lant", which is the last 4 letters. It cuts off the first 4 letters of eggplant.
    }
    public static void thirtythree() {
        System.out.println("33. \"kale\".charAt(3)");
        // My guess is it will say e, because it's the third letter, accounting for 0.
        System.out.println("kale".charAt(3));
    }

    public static void thirtyfour() {
        System.out.println("34. \"eggplant\".substring(\"eggplant\".length() - 1)");
        // My guess is it will say "t", because it cuts off the first 7 letters.
        System.out.println("eggplant".substring("eggplant".length() - 1));
    }
    public static void thirtyfive() {
        System.out.println("35. \"beans\".substring(1, 4)");
        // My guess is it will say "ean" because it keeps the middle 3 characters.
        System.out.println("beans".substring(1, 4));
    }
    public static void thirtysix() {
        boolean a = true;
        System.out.println("36. !a == true");
        // It will be true if a is false, and false if a is true.
        System.out.println(!a == true);
    }
    public static void thirtyseven() {
        boolean a = true;
        System.out.println("37. !a != false");
        /* It will be false if a is true, and true if a is false because != means not equal, so false not equals
        false is false because false = false.*/
        System.out.println(!a != false);
    }
    public static void thirtyeight() {
        boolean a = true;
        System.out.println("38. true && !a");
        // It will say false if a is true, and true if a is false because both have to be true if it's an &&.
        System.out.println(true && !a);
    }
    public static void thirtynine() {
        boolean a = true;
        int n = 3;
        System.out.println("39. if (n == 3) a = true ; else a = false; ");
        // a will equal false at the end if n is not 3, and true if it is.
        if (n == 3) {
            a = true;
        } else {
            a = false;
        }
        System.out.println(a);
    }
    public static void fourty() {
        boolean a = true;
        int n = 3;
        System.out.println("40. (n != 3) a = false; else a = true ;");
        /* a will equal false at the end if n is not 3, and true if it is. This is the same as the last problem
        except the a = statements are switched and the n statement has a not. */
        if (n != 3) {
            a = false;
        } else {
            a = true;
        }
        System.out.println(a);
    }
    public static void fourtyone() {
        boolean a = false;
        int n = 3;
        System.out.println("41. a = false; if (n > 3) if (n < 5) a = true;");
        // This question is worded weird, so I'm writing this how I am guessing it is supposed to be solved.
        // If n is between 3 and 5, a will be true, otherwise it will be false since a starts as false.
        if (n > 3 && n < 5) {
            a = true;
        }
        System.out.println(a);
    }
    public static void fourtytwo() {
        boolean a = false;
        int n = 0;
        System.out.println("42. if (n < 0) a = true; else a = (n > 1); ");
        // This will say true if n is less than 0, and false if n = 0.
        if (n < 0) {
            a = true;
        } else {
            a = (n > 1);
        }
        System.out.println(a);
    }
    public static void fourtythree() {
        int n = 6;
        System.out.println("43. n < 5 || n > 3");
        // It will say true for all values due to the way "or" works. There will never be 2 falses.
        System.out.println(n < 5 || n > 3);
    }
    public static void fourtyfour() {
        int n = 0;
        System.out.println("44. n < 3 && n > 5");
        // It will say false for all values because if a number is less than 3 to make the left true, it can't be greater than 5.
        System.out.println(n < 3 && n > 5);
    }
    public static void fourtyfive() {
        System.out.println("45. Can every while loop be expressed as a for loop and if so how?");
        // Every while loop can be expressed as a for loop. Here's an example of a while loop behaving like a for loop.
        int x = 0;
        while (x < 10) {
            x++;
        }
        System.out.println(x);

        //and here's a for loop that is the same.
        int y = 0;
        for (int i = 0; i < 10; i++) {
            y++;
        }
        System.out.println(y);
    }
    public static void fourtysix() {
        System.out.println("46. Can every while loop be expressed as a for loop and if so how?");
        // I don't think that a do while can be expressed as a while loop because of how java just handles loops.
        // A do while is fundamentally different than a while, and can't be replicated.
        int x = 0;
        int y = 0;
        do {
            System.out.println(x);
            x++;
        } while (x < 10);
        System.out.println(x);

        while (y < 10) {
            System.out.println(y);
            y++;
        }
    }
    public static void fourtyseven() {
        int m = 18, n = 10;
        System.out.println("47. int m = 18, n = 10; if (m > 10) { if (m > 5) n = 1; } else n = 2;");
        // n will be 1 because m is greater than both 10 and 5, fulfilling the requirements for n wo be set to 1.
        if (m > 10) { if (m > 5) n = 1; } else n = 2;
        System.out.println(n);
    }
    public static void fourtyeight() {
        int m = 18, n = 10;
        System.out.println("48. int m = 18, n = 10; if (m > 10) if (m > 5) n = 1; else n = 2;");
        // n will be 1 for the same reason as the problem above
        if (m > 10) if (m > 5) n = 1; else n = 2;
        System.out.println(n);
    }
    public static void fourtynine() {
        int m = 18, n = 10;
        System.out.println("49. if (m < 10) { if (m > 5) n = 1; } else n = 2;");
        // n will be 2 because m isn't less than 10, which activates the else, making n 2.
        if (m < 10) { if (m > 5) n = 1; } else n = 2;
        System.out.println(n);
    }
    public static void fifty() {
        int m = 18, n = 10;
        System.out.println("50.  if (m < 10) if (m > 5) n = 1; else n = 2");
        // I believe that this one is 10 because neither the if statements or the else statement are activated since the
        // else is not in curly braces.
        if (m < 10) if (m > 5) n = 1; else n = 2;
        System.out.println(n);
    }
    public static void fiftyone() {
        System.out.println("51. What’s going on? Why the difference? What effect does this have on your programming in Java?");
        // I believe that this is the case due to how the command line interface reads java programming vs how
        // a compiler compiles a program to be run. I'm not entirely sure about this, but this is the only explanation
        // that I can think of. If the command line interface one was written as "tomato".equals("tomato"),
        // it would work. (I think)
    }
    public static void fiftytwo() {
        System.out.println("52. Make up an example in Java that demonstrates what is known as \"the dangling else problem\" using the following statement: \"A student with a GPA of at least 1.5, but less than 2, is on probation. With less than 1.5, the student is failing.\"");
        double gpa = 1.5;
        boolean pass = false;
        if (gpa < 2.0 && gpa > 1.5) {
            pass = true;
        } else {
            pass = false;
        }
        System.out.println(pass);
        // I don't really understand this problem, but I made an if statement of what I think that this is asking for.
    }
}
