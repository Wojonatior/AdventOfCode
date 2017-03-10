#include "day1.h"
#include "day2.h"
#include "day3.h"
#include <string>
#include <iostream>

void day_header(std::string day_name){
    std::cout << "\n\n-----" << day_name << "-----\n";
}

int main() {
    day_header("Day 1");
    solve_day1();
    day_header("Day 2");
    solve_day2();
    day_header("Day 3");
    solve_day3();
    return 0;
}

