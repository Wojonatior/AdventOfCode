//
// Created by Jarek Wojciechowski on 3/10/17.
//
#include "day3.h"
#include <iostream>
#include <fstream>

class triangle{
    int sides[3];
public:
    triangle(int side1, int side2, int side3){
        sides[0] = side1;
        sides[1] = side2;
        sides[2] = side3;
    }
    bool is_valid_triangle(){
        //Check each of the sets of sides for validity
        return (sides[0]+sides[1] > sides[2] &&
                sides[1]+sides[2] > sides[0] &&
                sides[2]+sides[0] > sides[1]);
    }
};
int solve_day3(){
    FILE *fp;
    if ((fp = fopen("day2input.txt", "r+")) == NULL) {
        printf("File doesn't exist\n");
        exit(1);
    }

    int side1, side2, side3;
    int valid_triangles = 0;

    while (fscanf(fp, "%d %d %d", &side1, &side2, &side3) == 3) {
        if(triangle(side1, side2, side3).is_valid_triangle()){
            valid_triangles++;
        }
    }

    std::cout << "Number of valid triangles: " << valid_triangles;
}
