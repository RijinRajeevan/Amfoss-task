#include <stdio.h>

int main() {
    FILE *fx1, *fx2;
    int n, x;

    fx1 = fopen("input.txt", "r");
    fx2 = fopen("output.txt", "w");

    if (fx1 != NULL && fx2 != NULL) {
        fscanf(fx1, "%d", &n);
        fclose(fx1);

        x = (n / 2) + 1;

        for (int i = 1; i <= x; i++) {
            for (int j = 1; j <= (n - i) - 2; j++) {
                fputc(' ', fx2);
            }
            for (int j = 1; j <= (2 * i - 1); j++) {
                fputc('*', fx2);
            }
            fputc('\n', fx2);
        }

        for (int i = x - 1; i > 0; i--) {
            for (int j = 1; j <= (n - i) - 2; j++) {
                fputc(' ', fx2);
            }
            for (int j = 1; j <= (2 * i - 1); j++) {
                fputc('*', fx2);
            }
            fputc('\n', fx2);
        }

        fclose(fx2);
    }

    return 0;
}

