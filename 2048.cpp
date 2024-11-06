#include "2048.h"
#include <stdio.h>

extern "C"{

    void myprint()
    {
        printf("hello world\n");
    }

    int add(int num,  int num2){
        return num + num2;
    }


}