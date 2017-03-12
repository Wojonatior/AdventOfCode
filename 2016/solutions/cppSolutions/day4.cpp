//
// Created by Jarek Wojciechowski on 3/12/17.
//
#include <iostream>

class room{
    std::string full_room_name;
    std::string room_name;
    std::string given_checksum;
    std::string generated_checksum;
    int sector_id;
    int frequencyList[26] = {{0}};

    room(){
        // room_name = first portion of string
        // given checksum = portion inside brackets
        // sector_id = number before brackets
    }

    void generate_checksum(){}
        // Process room name
        // Convert into frequency list
        // Sort frequencies
        // Created generated checksum
    int sector_id_if_valid(){}
        // return sector_id if generated = given or 0

    void shift_room(){}
};


int solve_day4(){
    //read line from file
    //turn into room
    //generate checksum
    //validate checksum
}
