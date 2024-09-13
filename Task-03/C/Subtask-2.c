#include <stdio.h>

int main() {
    FILE *fx1, *fx2;
    
    fx1 = fopen("input.txt", "r");
    fx2 = fopen("output.txt", "w");
    
    if (fx1 != NULL && fx2 != NULL) {
        char ch;
        while ((ch = fgetc(fx1)) != EOF) {
            fputc(ch, fx2);
        }
        
        fclose(fx1);
        fclose(fx2);
    }

    return 0;
}

