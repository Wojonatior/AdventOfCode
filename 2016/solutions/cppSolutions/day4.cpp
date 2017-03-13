//
// Created by Jarek Wojciechowski on 3/12/17.
//
#include <iostream>
#include <regex>

class room{
    std::string full_room_name;
    std::string room_name;
    std::string given_checksum;
    std::string generated_checksum = "";
    int sector_id;
    std::vector<std::pair<char, int>> frequency_list;
public:

    room(std::string full_room_name){
        std::cmatch response;
        std::regex regex("([\\w|-]*?)(\\d*)\\[(\\w*)\\]");
        std::regex_search(full_room_name.c_str(), response, regex);
        //aaaaa-bbb-z-y-x-123[abxyz]
        room_name = response[1];
        room_name.erase(std::remove(room_name.begin(), room_name.end(), '-'), room_name.end());
        sector_id = std::stoi(response[2]);
        given_checksum = response[3];

        //init frequency_list
        for(int i=0; i < 26; ++i)
            frequency_list.push_back({'a' + i, 0});
    }

    void generate_checksum(){
        // Convert into frequency list
        for(int i=0; i<room_name.length(); i++)
            frequency_list[room_name[i]-'a'].second++;
        // Sort frequencies
        // stable sort to preserve alphabetic order
        std::stable_sort(frequency_list.begin(), frequency_list.end(), [](std::pair<char,int> left, std::pair<char,int> right) {
            return left.second > right.second;
        });
        // Compose checksum
        for(int i=0; i<5; i++)
            generated_checksum += frequency_list[i].first;
        return;
    }

    // return sector_id if generated = given or 0
    int sector_id_if_valid(){
        if(generated_checksum == given_checksum){ return sector_id; }
        else{ return 0;}
    }

    bool is_north_pole(){
        std::string shifted_room = room_name;
        for(int i=0; i<shifted_room.length(); i++){
            shifted_room[i] = ((shifted_room[i] - 'a' + sector_id) % 26) + 'a';
        }
        std::regex regex(".*north.*");
        return std::regex_search(shifted_room.begin(), shifted_room.end(), regex);
    }
};


int solve_day4(){
    FILE *fp;
    if ((fp = fopen("day4input.txt", "r+")) == NULL) {
        printf("File doesn't exist\n");
        exit(1);
    }

    char temp_cstr[256];
    std::string room_name;
    int room_id_count = 0;
    int room_id;
    int north_pole_id = 0;

    while (fscanf(fp, "%s", &temp_cstr) > 0) {
        room_name = temp_cstr;
        room tempRoom = room(room_name);

        tempRoom.generate_checksum();
        room_id = tempRoom.sector_id_if_valid();
        room_id_count += room_id;
        if(tempRoom.is_north_pole()){north_pole_id = room_id;}
    }

    std::cout << "Sum of valid Room IDs: " << room_id_count;
    std::cout << "\nRoom ID of North Pole room: " << north_pole_id;
}
