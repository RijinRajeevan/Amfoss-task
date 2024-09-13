
#include <stdio.h>
#include <math.h>
void main() {
int row;
printf("enter no. of rows:");
scanf("%d",&row);
int x = floor(row/2);
for(int i =1;i<=x+1;i++){
    for(int j =1;j<=(row-i)-2;j++){
        printf(" ");
            }
    for(int j =1;j<=(2*i)-1;j++){
        printf("*");
            }
    printf("\n");
        }
for(int i= x;i>=0;i--){
    for(int j =1;j<=(row-i)-2;j++){
        printf(" ");
            }
    for(int j =1;j<=(2*i)-1;j++){
        printf("*");
            }
    printf("\n");
        }


}
