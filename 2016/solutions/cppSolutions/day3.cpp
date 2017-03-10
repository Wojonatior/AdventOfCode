//
// Created by Jarek Wojciechowski on 3/10/17.
//
#include "day3.h"
#include <iostream>
#include <fstream>
#include <vector>

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
        return (sides[0] + sides[1] > sides[2] &&
                sides[1] + sides[2] > sides[0] &&
                sides[2] + sides[0] > sides[1]);
    }
};
int solve_day3(){
    FILE *fp;
    if ((fp = fopen("day3input.txt", "r+")) == NULL) {
        printf("File doesn't exist\n");
        exit(1);
    }

    int side1, side2, side3;
    int valid_triangles_pt1 = 0;
    int valid_triangles_pt2 = 0;
    std::vector<int> value_buffer;

    while (fscanf(fp, "%d %d %d", &side1, &side2, &side3) == 3) {
        if(triangle(side1, side2, side3).is_valid_triangle()){ valid_triangles_pt1++; }
        value_buffer.push_back(side1);
        value_buffer.push_back(side2);
        value_buffer.push_back(side3);
        if(value_buffer.size() == 9){
            if(triangle(value_buffer[0], value_buffer[3], value_buffer[6]).is_valid_triangle()){ valid_triangles_pt2++; }
            if(triangle(value_buffer[1], value_buffer[4], value_buffer[7]).is_valid_triangle()){ valid_triangles_pt2++; }
            if(triangle(value_buffer[2], value_buffer[5], value_buffer[8]).is_valid_triangle()){ valid_triangles_pt2++; }
            value_buffer.clear();
        }
    }

    std::cout << "Number of valid triangles: " << valid_triangles_pt1;
    std::cout << "\nNumber of valid transposed triangles: " << valid_triangles_pt2;
}
