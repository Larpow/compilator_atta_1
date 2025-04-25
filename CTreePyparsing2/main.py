import os
import sys

from compiler_demo import program


def main() -> None:
    prog1 = '''
        int input_int(string name) {
            if (name != "") {
                print("Введите " + name + ": ");
            }
            return to_int(read());
        }
        float input_float(string name) {
            if (name != "") {
                print("Введите " + name + ": ");
            }
            return to_float(read());
        }

        int g, g2 = g, g4 = 90;

        int a = input_int("a");
        float b = input_float("b"), c = input_float("c");  /* comment 1
        int d = input_int("d");
        */
        for (int i = 0, j = 8; ((i <= 5)) && g; i = i + 1, print(5))
            for(; a < b;)
                if (a > 7 + b) {
                    c = a + b * (2 - 1) + 0;  // comment 2
                    string bb = "98\tура";
                }
                else if (a)
                    print((c + 1) + " " + 89.89);
        for(bool i = true;;);

        int z;
        z=0;
    '''
    prog2 = 'int f1(int p1, float p2) { string a = p1 + p2; int x; }'''
    prog3 = 'for (;;);'
    prog4 = 'int i; i = 5;'
    prog5 = '''
        int input_int(string name) {
            if (name != "") {
                print("Введите " + name + ": ");
            }
            return to_int(read());

            // bool a() { }
        }
        int input_int2(string name, int a, int name2) {
            if (name != "") {
                print("Введите " + name + ": ");
            }
            return "";
        }
    '''
    prog6 = '''
            while(true){
                if (a>0){
                a = a+1;
                }
            }
        '''
    prog7 = '''
                switch (x) {
                    case 1:
                        a = 10;
                    case 2:
                        a = 20;
                    default:
                        a = 30;
                }
            '''
    prog8 = '''int main() {
    // 1. Объявление переменных
    int x = 5;
    float y = 3.14;
    string text = "Hello";
    bool flag = true;
    
    // 2. Условный оператор if-else
    if (x > 10) {
        text = "Large";
    } else if (x > 5) {
        text = "Medium";
    } else {
        text = "Small";
    }
    
    // 3. Цикл while
    int i = 0;
    while (i < 3) {
        print(text);
        i = i + 1;
    }
    
    // 4. Цикл for
    for (int j = 0; j < 5; j = j + 1) {
        y = y * 1.1;
    }
    
    // 5. Оператор switch (новый)
    switch (x) {
        case 1:
            text = "One";
        case 2:
            text = "Two";
        case 3:
            text = "Three";
        case 4:
            text = "Four";
        case 5:
            text = "Five";
        default:
            text = "Unknown";
    }
    
    // 6. Вложенные конструкции
    if (flag) {
        for (int k = 0; k < 2; k = k + 1) {
            switch (k) {
                case 0:
                    print("First iteration");
                case 1:
                    print("Second iteration");
            }
        }
    }
    
    // 7. Возврат значения из функции
    return 0;
}

// 8. Дополнительная функция
void print(string message) {
    // Вызов функции
    log(message);
}'''

    program.execute(prog8)


if __name__ == "__main__":
    main()
